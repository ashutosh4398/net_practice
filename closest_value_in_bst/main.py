class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def place_current_node_at_appropriate_pos(root, new_node):
    ''' 
        Function to construct BST
    
                10
                /\
               7  14
              /\  /\
             6 8 13 15
            /
           3
           \
           5 
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

def findClosestValueInBst(tree, target):
    if tree == None:
        return None
    parent_dist, left_dist, right_dist = -1, 10000, 10000
    parent_dist = abs(tree.value - target)
    
    if tree.left:
        left_dist = abs(tree.left.value - target)
    if tree.right:
        right_dist = abs(tree.right.value - target)
    
    child = "left" if left_dist < right_dist else "right"
    if child == "left":
        returned_elem = findClosestValueInBst(tree.left, target)
    if child == "right":
        returned_elem = findClosestValueInBst(tree.right, target)
    if returned_elem is None:
        return tree.value
    if abs(returned_elem-target) <parent_dist:
        return returned_elem
    return tree.value
    # if returned_dist < parent_dist:
    #     return returned_dist, returned_elem
    # else:
    #     return parent_dist, tree.value
    


cases = [
    (([10, 7, 14, 6, 8, 13, 15, 3, 5],2), 3),
    (([10, 5, 15, 2, 5, 13, 22, 1, 14], 12), 13)
]



for case in cases:
    arguments = case[0]
    root = construct(arguments[0])
    res = findClosestValueInBst(root, target=arguments[1])
    print(res, case[1])
