"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in 
the array, and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) time and O(n) space
        visited = {}
        for i in nums:
            if i in visited:
                return True
            visited[i] = 1
        return False
    
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # O(nlogn) time and O(1) space
    #     nums.sort()
    #     for i in range(0, len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False
        
