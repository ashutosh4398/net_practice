"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""
from typing import List, Dict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # get count
        nums1_lookup: Dict[int, int] = {}
        for num in nums1:
            nums1_lookup[num] = nums1_lookup.get(num, 0) + 1
        commons: List[int] = []
        for num in nums2:
            if num in nums1_lookup and nums1_lookup[num] != 0:
                commons.append(num)
                nums1_lookup[num] -= 1
        return commons

def main():
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))

if __name__ == "__main__":
    main()