"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) time and O(n) => space complexity (to convert it to list for sorting)
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        for s_i, t_j in zip(s,t):
            if s_i != t_j:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencies = {"s": {}, "t": {}} # O(2n)
        for i in s:
            frequencies["s"][i] = frequencies["s"].get(i, 0) + 1
        for i in t:
            frequencies["t"][i] = frequencies["t"].get(i, 0) + 1
        # comparing 
        for key,val in frequencies["s"].items():
            # if char not present
            if key not in frequencies["t"]:
                return False
            # if chat present but frequency does not match
            if frequencies["t"][key] != val:
                return False
        return True
        
