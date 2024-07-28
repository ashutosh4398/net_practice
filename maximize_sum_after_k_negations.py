"""
1005. Maximize Sum Of Array After K Negations

Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Constraints:

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104

"""

import unittest
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        for i in range(len(nums)):
            # we are making sure that there no negative number left
            # along with non-zero k value
            if nums[i] < 0 and k > 0:
                nums[i] = -1 * nums[i]
                k = k - 1
        # keep applying remaining negations on smallest positive numbers
        # since we are allowed to perform negations on same index
        # if k is even -> it will keep the same value
        if k%2 == 0:
            return sum(nums)

        nums.sort()
        # while k > 0:
        #     nums[0] = nums[0] * -1
        #     k -= 1
        # the above logic can be summarized in below step
        nums[0] = nums[0] * -1
        return sum(nums)


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test_case_1(self):
        self.assertEqual(self.s.largestSumAfterKNegations(nums=[4, 2, 3], k=1), 5)

    def test_case_2(self):
        self.assertEqual(self.s.largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3), 6)

    def test_case_3(self):
        self.assertEqual(
            self.s.largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2), 13
        )


if __name__ == "__main__":
    unittest.main()
