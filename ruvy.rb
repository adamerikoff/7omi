require "fileutils"
require "pathname"

require_relative "./blob"
require_relative "./db"
require_relative "./workspace"
require_relative "./entry"
require_relative "./tree"
require_relative "./author"
require_relative "./commit"


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

  entries = workspace.list_files.map do |path|
    data = workspace.read_file(path)
    blob = Blob.new(data)

    database.store(blob)

    Entry.new(path, blob.oid)
  end

  tree = Tree.new(entries)
  database.store(tree)

  name = ENV.fetch("USER")
  email = ENV.fetch("USER")
  author = Author.new(name, email, Time.now)

  puts "Enter commit message: "
  message = $stdin.gets.chomp


  commit = Commit.new(tree.oid, author, message)
  database.store(commit)

  File.open(ruvy_path.join("HEAD"), File::WRONLY | File::CREAT) do |file|
    file.puts(commit.oid)
  end

  puts "[(root-commit) #{ commit.oid }] #{ message.lines.first }"
  exit 0
else
  $stderr.puts "ruvy: '#{ command }' is not a jit command."
  exit 1
end
