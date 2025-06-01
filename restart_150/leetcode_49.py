"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n*m) -> n=len(strs), m=len(max string in strs)
        def arrange_string(string: str) -> str:
            # time complexity => O(m) -> m is len of string
            if len(string) <= 1:
                return string
            str_list = sorted(string)
            count = 1
            output = ""
            for i in range(0, len(string)-1):
                if str_list[i] == str_list[i+1]:
                    count += 1
                    continue
                output += f"{str_list[i]}{count}"
                count = 1
            output += f"{str_list[i+1]}{count}"
            return output
        visited = {} # reformed_str: [og_strs] -> space: O(n) -> n => len of strs
        for string in strs:
            reformed_string = arrange_string(string)
            visited[reformed_string] = visited.get(reformed_string, []) + [string]
        return list(visited.values())
        

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams([""]))