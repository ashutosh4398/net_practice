"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

"""

import math

# 4^x = n
# PLEASE NOTE, THE LOG IS TO THE BASE 4
# log(4^x) = log(n)
# x*1 = log(n)
# x = log(n)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # handling domain errors
        if n <= 0:
            return False
        x = int(math.log(n, 4))
        return n == 4**x

s = Solution()
print(s.isPowerOfFour(2))
