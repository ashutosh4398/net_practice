"""
257. Binary Tree Paths
Easy
Topics
Companies
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_leaf_node(self, node):
        return node.left is None and node.right is None

    def _helper(self, node: Optional[TreeNode], path: str, solutions = None):
        if not solutions:
            solutions = []
        if not node:
            return solutions
        path += (f"->{node.val}") if path else str(node.val)
        if self.is_leaf_node(node):
            solutions.append(path)
            return solutions
        return self._helper(node.left, path) + self._helper(node.right, path)
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self._helper(node=root, path="")
    
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(t))
