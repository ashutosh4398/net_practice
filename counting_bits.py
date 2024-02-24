"""
338. Counting Bits
Easy
Topics
Companies
Hint
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""


from typing import List
import math
class Solution:
    def count_bit_representation(self, n: int) -> int:
        # since it is binary system
        bits = round(math.log(n, 2),1)
        if n == 2**bits:
            return int(bits + 1)
        return int(math.ceil(bits))
    
    # 8 -> 4 ie 2**
    def create_number_pool_desc(self, n: int) -> List[int]:
        # 2^(n-1), ... 2^0
        bits = self.count_bit_representation(n)
        return [2**i for i in range(bits-1,-1,-1)]

    def countBits(self, n: int) -> List[int]:
        bits_pool: List[int] = self.create_number_pool_desc(n)
        final_output: List[int] = []
        for i in range(n+1):
            total = count = 0
            for j in bits_pool:
                if total + j <= i:
                    total += j
                    count += 1
                if total == i:
                    break
            final_output.append(count)

        return final_output



class EfficientSolution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp

if __name__ == "__main__":
    s = EfficientSolution()
    print(s.countBits(2))