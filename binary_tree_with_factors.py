"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.

"""

from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        possible_ways = {node: 1 for node in arr}
        arr.sort()
        for i,parent_node in enumerate(arr):
            ways = 0
            for j,node in enumerate(arr[:i]):
                if parent_node % node != 0:
                    continue
                other_node = parent_node / node
                if other_node not in possible_ways:
                    continue
                ways += possible_ways[other_node] * possible_ways[node]
            
            possible_ways[parent_node] = possible_ways[parent_node] + ways
        return sum(possible_ways.values()) % ((10**9) + 7)


def main():
    s = Solution()
    print(s.numFactoredBinaryTrees([2,4]))
    print(s.numFactoredBinaryTrees([2,4,5,10]))

if __name__ == "__main__":
    main()