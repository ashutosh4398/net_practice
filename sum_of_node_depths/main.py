from tree_utils import construct_example_tree

def nodeDepths(root):
    return nodeDepthUtil(root, currentDepth=-1, depth_sum=0)


def nodeDepthUtil(node, currentDepth, depth_sum):
    if node is None:
        return depth_sum

    currentDepth += 1
    depth_sum += currentDepth
    depth_sum = nodeDepthUtil(node.left, currentDepth, depth_sum)
    depth_sum = nodeDepthUtil(node.right, currentDepth, depth_sum)
    return depth_sum

root = construct_example_tree()
depth_sum = nodeDepths(root)
print(depth_sum)