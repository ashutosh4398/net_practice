# Closest Value in BST

**Constructing BST**

```python
# pseudo code
arr = [10, 7, 14, 6, 8, 13, 15, 3, 5]

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def place_current_node_at_appropriate_pos(root, new_node):
    ''' 
        Function to place new node at correct position
    
                10
                /\
               7  14
              /\  /\
             6 8 13 15
    '''
    if root is None:
        # to indicate insertable position
        return new_node
    if new_node.value < root.value:
        root.left = place_current_node_at_appropriate_pos(root.left, new_node)
    elif new_node.value >= root.value:
        root.right = place_current_node_at_appropriate_pos(root.right, new_node)
    return root

def construct(arr):
    '''
        Function to construct bst from specified array and returns root element
    '''
    root = None
    for each in arr:
        if root is None:
            root = BST(each)
            continue
        if root is not None:
            new_node = BST(each)
            _ = place_current_node_at_appropriate_pos(root, new_node)
    return root

```

**Solution**
- Let `(root.value-target)` be 'R1'
- Let `(root.left.value - target)` be C1
- Let `(root.right.value - target)` be C2

- if R1 is less that C1 & C2 return `root.value`
- if C1 is less than R1 and C2, traverse root.left
- if C2 is less than R1 and C1, traverse root.right

if we reach leaf node while traversing, return that leaf node which is indicated by false
if parent's distance is less than direct children, then return parent's value as answer

```Python
def closestValue(tree, target):
    if tree is None:
        return False
    parent_dist, left_dist, right_dist = -1, 10000, 10000
    parent_dist = tree.value - target
    
    if tree.left:
        left_dist = tree.left.value - target
    if tree.right:
        right_dist = tree.right.value - target
    
    min_dist, child = (left_dist, "left") if left_dist > right_dist else (right_dist, "right")
    
    if parent_dist < min_dist:
        return tree.value
    if child == "left":
        resp = closestValue(tree.left, target)
    if child == "right":
        resp = closestValue(tree.right, target)

    if resp == False:
        return tree.value
    return resp

```