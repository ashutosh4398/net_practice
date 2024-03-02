"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
"""

from typing import List

class Solution:
    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    #     removed_count = 0
    #     for idx, interval in enumerate(intervals):
    #         for sub_idx, sub_interval in enumerate(intervals):
    #             if idx == sub_idx:
    #                 continue
    #             if interval[0] >= sub_interval[0] and interval[1] <= sub_interval[1]:
    #                 removed_count += 1
    #                 break

    #     return len(intervals) - removed_count
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort in increasing order and in case of tie, consider the interval with higher end value
        intervals.sort(key=lambda i: (i[0], -i[1]))
        res = [intervals[0]]
        for l,r in intervals[1:]:
            prev_left, prev_right = res[-1]
            # current (l,r) is covered by previous interval
            if prev_left <= l and prev_right >= r:
                continue
            res.append([l,r])
        return len(res)


def main():
    s = Solution()
    print(s.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
    print(s.removeCoveredIntervals([[1,4],[2,3]]))
    print(s.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))


if __name__ == "__main__":
    main()