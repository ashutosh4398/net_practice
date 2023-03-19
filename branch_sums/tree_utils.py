
# node definition
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def arrange_new_node(new_node, parent):
    if new_node.value < parent.value:
        direction = "left"
    if new_node.value > parent.value:
        direction = "right"
    if getattr(parent, direction):
        return arrange_new_node(new_node, getattr(parent, direction))
    setattr(parent, direction, new_node)
    return

def create_tree(nodes):
    root = None
    for node in nodes:
        n = Node(node)
        if root is None:
            root = n
            continue
        arrange_new_node(n, root)
    return root

def traverse(parent):
    if parent is None:
        return
    traverse(parent.left)
    print(parent.value)
    traverse(parent.right)
    return

    