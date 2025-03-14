"""
680. Valid Palindrome II
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

acba =>
accbpa =>

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    def is_actual_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        allowed_deletions = 2
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif allowed_deletions > 0:
                allowed_deletions -= 1
                return self.is_actual_palindrome(
                    s[left + 1 : right + 1]
                ) or self.is_actual_palindrome(s[left:right])
            else:
                return False
        return True


s = Solution()
print(s.validPalindrome("apmmpa"))
