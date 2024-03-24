"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expanding from center
        pal = ""
        pal_len = 0

        # handling odd lengths palindrome
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                str_len = r - l + 1
                if str_len > pal_len:
                    pal_len = r - l + 1
                    pal = s[l : r + 1]
                l -= 1
                r += 1

        # handling even length palindromes
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                str_len = r - l + 1
                if str_len > pal_len:
                    pal_len = r - l + 1
                    pal = s[l : r + 1]
                l -= 1
                r += 1
        return pal


def main():
    s = Solution()
    print(s.longestPalindrome("abbc"))


if __name__ == "__main__":
    main()
