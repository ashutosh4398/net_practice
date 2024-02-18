"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

"""

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = round(math.log(n,3), 3)
        return n == 3 ** x
 
s = Solution()
# print(s.isPowerOfThree(27))
# print(s.isPowerOfThree(0))
# print(s.isPowerOfThree(-1))
print(s.isPowerOfThree(243))
