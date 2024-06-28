require "fileutils"
require "pathname"

require_relative "./blob"
require_relative "./db"
require_relative "./workspace"

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

  workspace.list_files.each do |path|
    data = workspace.read_file(path)
    blob = Blob.new(data)
    database.store(blob)
  end
else
  $stderr.puts "ruvy: '#{ command }' is not a jit command."
  exit 1
end
