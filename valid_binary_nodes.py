"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1

"""

from typing import List

class Solution:    
    def check_cycle(self, parent, graph, visited):
        if parent in visited:
            return True
        visited.add(parent)
        for child in graph.get(parent, []):
            res = self.check_cycle(child, graph, visited)
            if res:
                return res
        return None


    def make_traversal_graph(self, mapping) -> dict:
        graph = {}
        for child, parent in mapping.items():
            children = graph.get(parent, [])
            children.append(child)
            graph[parent] = children
        return graph

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent_child_map = {}
        root_node = 0
        for idx, (l_child, r_child) in enumerate(zip(leftChild, rightChild)):
            parent = idx
            if l_child == root_node or r_child == root_node:
                root_node = idx
            if l_child != -1:
                if l_child in parent_child_map and parent_child_map[l_child] != parent:
                    return False
                parent_child_map[l_child] = parent
            
            if r_child != -1:
                if r_child in parent_child_map and parent_child_map[r_child] != parent:
                    return False
                parent_child_map[r_child] = parent
        graph = self.make_traversal_graph(parent_child_map)
        visited = set()
        return not self.check_cycle(root_node, graph, visited) and len(visited) == n
    
    
def main():
    s = Solution()
    # print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))
    # print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
    # print(s.validateBinaryTreeNodes(2, [1,0], [-1,-1]))
    # print(s.validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]))
    print(s.validateBinaryTreeNodes(4, [3,-1,1,-1], [-1,-1,0,-1]))
    

if __name__ == "__main__":
    main()