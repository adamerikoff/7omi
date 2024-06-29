require "digest/sha1"
require 'set'

require_relative "./index/entry"
require_relative "./lockfile"

class Index

  HEADER_FORMAT = "a4N2"

  def initialize(pathname)
    @entries = {}
    @keys = SortedSet.new
    @lockfile = Lockfile.new(pathname)
    clear
    end

    def add(pathname, oid, stat)
      entry = Entry.create(pathname, oid, stat)
      @keys.add(entry.key)
      @entries[entry.key] = entry
    end

  def write_updates
    return false unless @lockfile.hold_for_update

    begin_write
    header = ["DIRC", 2, @entries.size].pack(HEADER_FORMAT)
    write(header)
    @entries.each { |key, entry| write(entry.to_s) }
    finish_write

    true
  end

  def load_for_update
    if @lockfile.hold_for_update
      load
      true
    else
      false
    end
  end

  def load
    clear
    file = open_index_file

    if file
      reader = Checksum.new(file)
      count = read_header(reader)
      read_entries(reader, count)
      reader.verify_checksum
    end
  ensure
    file&.close
  end

  def clear
    @entries = {}
    @keys = SortedSet.new
    @changed = false
  end

  def open_index_file
    File.open(@pathname, File::RDONLY)
  rescue Errno::ENOENT
    nil
  end

  private

  def begin_write
    @digest = Digest::SHA1.new
  end

  def write(data)
    @lockfile.write(data)
    @digest.update(data)
  end

  def finish_write
    @lockfile.write(@digest.digest)
    @lockfile.commit
  end

  def each_entry
    @keys.sort.each { |key| yield @entries[key] }
  end

end
