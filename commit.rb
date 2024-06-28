class Commit
  attr_accessor :oid

  def initialize(tree, author, message)
    @tree = tree
    @author = author
    @message = message
  end

  def type
    "commit"
  end


  def to_s
    lines = [
      "TREE: #{ @tree }",
      "AUTHOR: #{ @author }",
      "COMMITER: #{ @author }",
      "",
      ["MESSAGE:", @message].join(" ")
    ]

    lines.join("\n")
  end
end
