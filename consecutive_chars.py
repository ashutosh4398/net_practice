"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.

"""
class Solution:
    def maxPower(self, s: str) -> int:
        current_pow = 1
        max_power = 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                current_pow += 1
            else:
                max_power = max(max_power, current_pow)
                current_pow = 1
        return max(max_power, current_pow)

def main():
    s = Solution()
    print(s.maxPower("leetcode"))
    print(s.maxPower("abbcccddddeeeeedcba"))

if __name__ == "__main__":
    main()