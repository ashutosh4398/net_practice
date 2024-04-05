"""
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

 

Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
 

Constraints:

1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
Both arrays contain unique ids.
Both arrays are in strictly ascending order by id.

"""

from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        ptr_n1 = ptr_n2 = 0
        n1_len, n2_len = len(nums1), len(nums2)
        result = []
        while ptr_n1 < n1_len and ptr_n2 < n2_len:
            [id1, val1], [id2, val2] = nums1[ptr_n1], nums2[ptr_n2]
            if id1 == id2:
                result.append([id1, val1 + val2])
                ptr_n1 += 1
                ptr_n2 += 1
            if id1 < id2:
                result.append([id1, val1])
                ptr_n1 += 1
            if id2 < id1:
                result.append([id2, val2])
                ptr_n2 += 1

        # check for remaining elements in either of the lists
        while ptr_n1 < n1_len:
            result.append(nums1[ptr_n1])
            ptr_n1 += 1
        while ptr_n2 < n2_len:
            result.append(nums2[ptr_n2])
            ptr_n2 += 1

        return result


def main():
    s = Solution()
    print(s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
    print(s.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))


if __name__ == "__main__":
    main()
