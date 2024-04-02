"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutives = 0
        consecutives = 1
        target = 1
        # EDGE CASES
        if len(nums) == 1:
            return 0 if 1 not in nums else 1
        # GENERAL CASES
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] == target:
                consecutives += 1
                continue
            max_consecutives = max(max_consecutives, consecutives)
            consecutives = 1
        
        return max(max_consecutives, consecutives) if target in nums else 0

def main():
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,0,1,1,1,0,1]))
    print(s.findMaxConsecutiveOnes([1]))
    print(s.findMaxConsecutiveOnes([0,0]))


if __name__ == "__main__":
    main()
            
