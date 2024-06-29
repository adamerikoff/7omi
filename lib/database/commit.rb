class Commit
  attr_accessor :oid

  def initialize(tree, parent, author, message)
    @tree = tree
    @parent = parent
    @author = author
    @message = message
  end

  def type
    "commit"
  end


  def to_s
    lines = [
      "TREE: #{ @tree }",
      "PARENT: #{ @parent.nil? ? "(root-commit) " : @parent }",
      "AUTHOR: #{ @author }",
      "COMMITER: #{ @author }",
      "",
      ["MESSAGE:", @message].join(" ")
    ]

    lines.join("\n")
  end
end
