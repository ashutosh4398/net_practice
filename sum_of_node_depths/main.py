from tree_utils import construct_example_tree

def nodeDepths(root):
    return nodeDepthUtil(root, currentDepth=0)


def nodeDepthUtil(node, currentDepth):
    if node is None:
        return 0
    
    left_depth_sum = nodeDepthUtil(node.left, currentDepth + 1)
    right_depth_sum = nodeDepthUtil(node.right, currentDepth + 1)
    return currentDepth + left_depth_sum + right_depth_sum

root = construct_example_tree()
depth_sum = nodeDepths(root)
print(depth_sum)