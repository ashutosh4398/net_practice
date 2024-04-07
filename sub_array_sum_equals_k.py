"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = {0: 1} # base case
        curr_sum = 0
        res = 0
        for i in nums:
            curr_sum += i
            diff = curr_sum - k
            res += pref_sum.get(diff, 0)
            pref_sum[curr_sum] = pref_sum.get(curr_sum, 0) + 1
        return res
            


def main():
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))
    print(s.subarraySum([1, 2, 3], 3))


if __name__ == "__main__":
    main()
