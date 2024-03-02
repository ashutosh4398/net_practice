"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

"""

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = [idx for idx, num in enumerate(nums) if num%2 != 0]
        odd_len = len(odd_indices)
        combinations = 0
        start = 0 # index refering to nums
        for idx, num in enumerate(odd_indices):
            if idx + k - 1 >= odd_len:
                break
            end = odd_indices[idx + k] - 1 if idx + k < odd_len else len(nums)-1
            odd_start, odd_end = num, odd_indices[idx + k - 1]
            combinations += max(1, odd_start-start+1) * max(1, end-odd_end+1)
            start = num + 1
        return combinations

s = Solution()
print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))