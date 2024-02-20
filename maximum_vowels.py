"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels, window_size = 0, 0
        current_window_vowels = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        # used a sliding window approach
        # for each window of size k, count current window vowels
        # as the window length is reached, find max vowel count
        # update the window vowel count by subtracting 1 if the starting character of window is a vowel
        for i in range(len(s)):
            if window_size == k:
                debug = s[i-window_size: i]
                max_vowels = max(max_vowels, current_window_vowels)
                # subtract 1 count to maintain window vowel count
                current_window_vowels -= 1 if s[i-window_size] in vowels else 0
                window_size = window_size - 1

            if s[i] in vowels:
                current_window_vowels += 1
            window_size += 1
        
        # edge case, if the window size is large, so it might not have counted the last char
        # hence returning the last encountered max with current window's vowel count
        return max(max_vowels, current_window_vowels)
    

s = Solution()
print(s.maxVowels("abciiidef", 3))
print(s.maxVowels("aeiou", 2))
print(s.maxVowels("leetcode", 3))
print(s.maxVowels("weallloveyou", 7))