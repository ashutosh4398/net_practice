from tree_utils import traverse, create_tree

def branchSums(root):
    # Write your code here.
    return branchSumUtils(root, sum_=0, sum_list=[])

def is_leaf_node(node):
    return (node.left is None) and (node.right is None)

def branchSumUtils(parent, sum_, sum_list):
    if parent is None:
        return
    
    sum_ += parent.value
    if is_leaf_node(parent):
        sum_list.append(sum_)
    
    branchSumUtils(parent.left, sum_, sum_list)
    branchSumUtils(parent.right, sum_, sum_list)
    # subtract the current node value after visiting
    # so that we can maintain sum
    sum_ -= parent.value
    return sum_list


# nodes = [1,2,3,4,5,6,7,8,9,10]
nodes = [8, 3, 10, 1, 6, 4]
root = create_tree(nodes)
# traverse(root)

print(branchSums(root))