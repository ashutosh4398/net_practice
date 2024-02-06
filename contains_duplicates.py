"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # (i -j) == k solution
        # num_len = len(nums)
        # for idx,num in enumerate(nums):
        #     if (idx + k) <= (num_len - 1 ) and num == nums[idx + k]:
        #         return True
        # return False

        # (i-j) <=k 
        hset = {}
        for idx,num in enumerate(nums):
            if num in hset and (idx - hset[num]) <= k:
                return True
            hset[num] = idx
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))
print(s.containsNearbyDuplicate([1,0,1,1],1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))