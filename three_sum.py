"""
15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List, Dict, Literal

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        target = 0
        triplets = set()
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    triplets.add((nums[i], nums[j], nums[k]))
                    break
                elif temp > target:
                    k -= 1
                else:
                    j += 1
        return [list(x) for x in triplets]



def main():
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

if __name__ == "__main__":
    main()