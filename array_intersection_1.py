"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

from typing import List, Optional


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(3n) including output array
        num1_lookup, num2_lookup = {}, {}
        for num in nums1:
            num1_lookup[num] = num1_lookup.get(num, 0) + 1
        for num in nums2:
            num2_lookup[num] = num2_lookup.get(num, 0) + 1

        common: List[int] = []
        for num, count in num1_lookup.items():
            if num in num2_lookup:
                common.append(num)
        return common

    def binarySearch(
        self,
        array: List[int],
        target: int,
        left: Optional[int] = 0,
        right: Optional[int] = None,
    ) -> int:
        if right is None:
            right = len(array) - 1

        if left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            if target < array[mid]:
                return self.binarySearch(array, target, left, mid - 1)
            if target > array[mid]:
                return self.binarySearch(array, target, mid + 1, right)
        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time complexity: O(nlogn)
        # space complexity: O(n) # just because of holding array
        # sort nums1, nums2
        # iterate over min array, search for element present in max array
        nums1 = sorted(nums1)  # nlog(n)
        nums2 = sorted(nums2)  # nlog(n)
        master, assitant = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        commons: set[int] = set()
        for num in master:
            idx = self.binarySearch(assitant, num)
            if idx != -1:
                commons.add(num)
        return list(commons)

def main():
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(s.intersection([1], [1]))


if __name__ == "__main__":
    main()
