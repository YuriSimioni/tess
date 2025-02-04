from rich.tree import Tree
from rich import print

tree = Tree("Rich Tree")
print(tree)

tree.add("foo")
tree.add("bar")
print(tree)

baz_tree = tree.add("baz")
baz_tree.add("[red]Red")

print(tree)