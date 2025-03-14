"""
1941. Check if All Characters Have Equal Number of Occurrences
Easy
Topics
Companies
Hint
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def create_mapping(self, s) -> dict:
        # maintaining count
        hash_map:dict = dict()
        for i in s:
            hash_map[i.lower()] = hash_map.get(i.lower(), 0) + 1
        return hash_map

    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = self.create_mapping(s)
        prev_key_val = None
        for k,v in hash_map.items():
            if prev_key_val is None:
                prev_key_val = v
                continue
            if prev_key_val != v:
                return False
        return True

s = Solution()
print(s.areOccurrencesEqual("abacbc"))