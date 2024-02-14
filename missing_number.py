"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


"""
# 0,1,2,3,4,5 => 15
# 6(7)/2 => 21
# 5(6)/2 => 15



from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_nums = len(nums) # since it includes 0, we treat as n + 1
        ideal_sum = ((total_nums+1)*total_nums)/2
        return int(ideal_sum - sum(nums))

    def otherSolution(self, nums: List[int]) -> int:
        n = len(nums)
        ideal_sum = sum([i for i in range(0, n+1)])
        actual_sum = sum(nums)
        return int(ideal_sum-actual_sum)

s = Solution()
print(s.otherSolution([3,0,1]))
print(s.otherSolution([0,1]))
print(s.otherSolution([9,6,4,2,3,5,7,0,1]))