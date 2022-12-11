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

arr = [10, 7, 14, 6, 8, 13, 15, 3, 5]
root = None
for each in arr:
    if root is None:
        root = BST(each)
        continue
    if root is not None:
        new_node = BST(each)
        _ = place_current_node_at_appropriate_pos(root, new_node)
