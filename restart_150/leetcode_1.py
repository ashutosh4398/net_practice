"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using additional space O(n) time and O(n) space
        visited = {}
        for idx, num in enumerate(nums):
            other_half = target - num
            if other_half in visited:
                return [idx, visited[other_half]]
            visited[num] = idx
        return []

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    #     def binary_search(nums, start, end, new_target):
    #         if start > end:
    #             return -1
    #         mid = (start+end)//2 #why this logic ?????
    #         if nums[mid] == new_target:
    #             return mid
    #         if nums[mid] > new_target:
    #             return binary_search(nums, start, mid-1, new_target)
    #         return binary_search(nums, mid+1, end, new_target)
        
    #     nums.sort()
    #     for idx,num in enumerate(nums):
    #         other_half = target - num
    #         print(other_half, idx, num)
    #         other_half_index = binary_search(nums, idx+1, len(nums)-1, other_half)
    #         if other_half != -1:
    #             return (idx, other_half_index)


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,2,4], 6))