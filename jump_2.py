"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""

from typing import List


MAX_STEPS = 1000000


class Solution:
    def __jump(self, nums: List[int], goal_pos: int, current_pos: int = 0, steps_taken=0, visited=None, min_path=None) -> int:
        if visited is None:
            visited = {}
        if min_path is None:
            min_path = [current_pos]
        # base cases
        if goal_pos == current_pos:
            return steps_taken
        if current_pos > goal_pos:
            return -1

        jump = nums[current_pos]
        min_steps = MAX_STEPS
        for i in range(jump, 0, -1):
            next_jump = current_pos + i
            if next_jump > goal_pos:
                continue
            if (current_pos, next_jump) in visited:
                steps = visited[(current_pos, next_jump)]
            else:
                steps = self.__jump(nums, goal_pos, next_jump, steps_taken + 1, visited)
            visited[(current_pos, next_jump)] = steps
            if steps == -1:
                continue
            min_steps = min(min_steps, steps)
            if min_steps == steps:
                min_path.append((nums[next_jump], min_steps))
        if current_pos == 0:
            print(min_path)
        return min_steps if min_steps != MAX_STEPS else -1

    def jump(self, nums: List[int]) -> int:
        return self.__jump(nums, len(nums) - 1, 0)


def main():
    s = Solution()
    # print(s.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
    # print(s.jump([2,3,1,1,4]))
    # print(s.jump([5,9,3,2,1,0,2,3,3,1,0,0]))
    # print(s.jump([5,4,0,1,3,6,8,0,9,4,9,1,8,7,4,8]))
    # print(s.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
    print(s.jump([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]))


if __name__ == "__main__":
    main()