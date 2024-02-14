"""
283. Move Zeroes
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0 # counter to track non-zeros and replace in array
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        if k == 0:
            return
        remaining = len(nums)-k 
        nums[k:] = [0 for _ in range(remaining)]
    
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([0]))
print(s.moveZeroes([]))
        