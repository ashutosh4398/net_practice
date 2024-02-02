"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
"""

l1 = []
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:    
        res = ""
        while columnNumber:
            offset = (columnNumber - 1) % 26
            res = chr(ord('A') + offset) + res
            columnNumber = (columnNumber - 1) // 26
        
        return res

s = Solution()
print(s.convertToTitle(701))