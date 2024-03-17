"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.

"""

class Solution:
    def reverse_substring(self, og_str, start_idx, end_idx):
        sub_str = og_str[start_idx+1: end_idx]
        return sub_str[::-1]
    
    def reverseParentheses(self, s: str) -> str:
        stack = []
        new_str = s
        for i in range(len(new_str)):
            if new_str[i] == "(":
                stack.append(i)
            if new_str[i] == ")":
                opening_idx = stack.pop()
                reverse_string = self.reverse_substring(new_str, opening_idx, i)
                new_str = new_str[:opening_idx+1] + reverse_string + new_str[i:]

        return new_str.replace("(", "").replace(")", "")
    
def main():
    s = Solution()
    print(s.reverseParentheses("(abcd)"))
    print(s.reverseParentheses("(u(love)i)"))
    print(s.reverseParentheses("(ed(et(oc))el)"))
    print(s.reverseParentheses("ashutosh"))
    
if __name__ == "__main__":
    main()