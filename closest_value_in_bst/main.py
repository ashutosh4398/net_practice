def findClosestValueInBst(tree, target):
    min_diff = None
    node = None
    while True:
        
        if tree is None:
            break
        diff = abs(tree.value - target)
        
        if min_diff is None or diff < min_diff:
            # print(tree.value)
            min_diff = diff
            node = tree.value
        if target >= tree.value:
            tree = tree.right
        else:
            tree = tree.left
    return node

def findClosestValueInBstRecursively(tree, target):
    return findClosestHelper(tree, target, closest=float("inf"))

def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if target > tree.value:
        return findClosestHelper(tree.right, target, closest)
    elif target < tree.value:
        return findClosestHelper(tree.left, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def arrange_node(new_node, parent):
    if new_node.value < parent.value:
        direction = "left"
    if new_node.value >= parent.value:
        direction = "right"
    if getattr(parent, direction) is not None:
        return arrange_node(new_node, getattr(parent, direction))
    else:
        setattr(parent, direction, new_node)

def traverse(root):
    if root is None:
        return
    traverse(root.left)
    print(root.value)
    traverse(root.right)
    

root = None

l = [10, 5, 15, 2, 5, 13, 22, 1, 14]

for i in l:
    node = BST(value=i)
    if root is None:
        root = node
        continue
    arrange_node(node, root)

# traverse(root)
print(findClosestValueInBst(root, target=12))
print(findClosestValueInBstRecursively(root, target=12))
