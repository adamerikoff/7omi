require "fileutils"
require "pathname"

require_relative "./lib/database/blob"
require_relative "./lib/database/tree"
require_relative "./lib/database/author"
require_relative "./lib/database/commit"

require_relative "./lib/db"
require_relative "./lib/workspace"
require_relative "./lib/entry"
require_relative "./lib/refs"
require_relative './lib/index'

command = ARGV.shift

case command
when "init"

  path = ARGV.fetch(0, Dir.getwd)
  root_path = Pathname.new(File.expand_path(path))
  ruvy_path = root_path.join(".ruvy")

  ["objects", "refs"].each do |dir|
    begin
      FileUtils.mkdir_p(ruvy_path.join(dir))
    rescue Errno::EACCES => error
      $stderr.puts "fatal: #{ error.message }"
      exit 1
    end
  end

  puts "Initialized empty RUVY repository in #{ ruvy_path }"
  exit 0

when "commit"

  root_path = Pathname.new(Dir.getwd)
  ruvy_path = root_path.join(".ruvy")
  db_path = ruvy_path.join("objects")

  workspace = Workspace.new(root_path)
  database = Database.new(db_path)
  refs = Refs.new(root_path)

  entries = workspace.list_files.map do |path|
    data = workspace.read_file(path)
    blob = Blob.new(data)

    database.store(blob)

    stat = workspace.stat_file(path)
    Entry.new(path, blob.oid, stat)
  end

  root = Tree.build(entries)
  root.traverse { |tree| database.store(tree) }

  parent = refs.read_head
  name = ENV.fetch("USER")
  email = ENV.fetch("USER")
  author = Author.new(name, email, Time.now)

  puts "Enter commit message: "
  message = $stdin.gets.chomp


  commit = Commit.new(root.oid, parent, author, message)
  database.store(commit)
  refs.update_head(commit.oid)

  is_root = parent.nil? ? "(root-commit) " : ""
  puts "[#{ is_root }#{ commit.oid }] #{ message.lines.first }"
  exit 0

when "add"

  root_path = Pathname.new(Dir.getwd)
  ruvy_path = root_path.join(".ruvy")
  db_path = ruvy_path.join("objects")
  index_path = ruvy_path.join("index")

  workspace = Workspace.new(root_path)
  database = Database.new(db_path)
  index = Index.new(index_path)

  index.load_for_update

  ARGV.each do |path_input|
    path = Pathname.new(File.expand_path(path_input))

    workspace.list_files(path).each do |pathname|
      data = workspace.read_file(pathname)
      stat = workspace.stat_file(pathname)

      blob = Database::Blob.new(data)
      database.store(blob)
      index.add(pathname, blob.oid, stat)
    end
  end

  index.write_updates
  exit 0
else
  $stderr.puts "ruvy: '#{ command }' is not a jit command."
  exit 1
end
