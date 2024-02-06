"""
2^0 + 2^1 + 2^2 + .... + 2^n
    = 2^(h+1) - 1

"""

"""
222. Count Complete Tree Nodes
Easy
Topics
Companies
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def countHeight(self, root: Optional[TreeNode]) -> int:
    #     # since it is complete bst, we will keep going left
    #     height = 0
    #     while root:
    #         height += 1
    #         root = root.left
    #     return height - 1
    
    # def getNodesAtNthLevel(self, root: Optional[TreeNode], level: int) -> List[TreeNode]:
    #     if level <= 0:
    #         return [root]
    #     elems_at_prev_level =  self.getNodesAtNthLevel(root, level-1)
    #     temp = []
    #     for elem in elems_at_prev_level:
    #         if elem.left:
    #             temp.append(elem.left)
    #         if elem.right:
    #             temp.append(elem.right)        
    #     return temp
    
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     tree_height = self.countHeight(root)
    #     if tree_height < 0:
    #         return 0
    #     max_nodes_at_second_last_level = (2 ** tree_height) - 1
    #     children = self.getNodesAtNthLevel(root, tree_height)
    #     return max_nodes_at_second_last_level + len(children)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.efficient_solution(root)
    
    def efficient_solution(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = right_height = 0
        left = right = root

        while left:
            left_height += 1
            left = left.left
        
        while right:
            right_height += 1
            right = right.right
        
        if left_height == right_height:
            return (2**(left_height+1-1)) - 1
        
        return 1 + self.efficient_solution(root.left) + self.efficient_solution(root.right)