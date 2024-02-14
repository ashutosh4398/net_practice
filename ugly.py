"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
 

Constraints:

-231 <= n <= 231 - 1

"""

# def find_prime_factors(n):
#     # O(sqrt(N))
#     factors = []
#     for i in range(2, int(n**0.5)):
#         while n % i == 0:
#             n = n / i
#             factors.append(i)
#     if n > 1:
#         factors.append(int(n))
#     return factors


# def sieve_algo(n):
#     # O(N*log(log(N)))
#     # O(N)
#     is_prime = [True for _ in range(n)]
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, n):
#         if is_prime[i]:
#             for j in range(i+i, n, i):
#                 is_prime[j] = False
    
#     for i in range(n):
#         print(i, is_prime[i])


class Solution:
    def isUgly(self, n: int) -> bool:   
        if n <= 0:
            n = n * -1
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True
    
s = Solution()
# print(s.isUgly(6))
# print(s.isUgly(1))
# print(s.isUgly(14))
print(s.isUgly(-2147483648))