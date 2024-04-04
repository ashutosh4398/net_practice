"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.

"""

class Solution:

    def consecutieve_count(self, name):
        temp = []
        count = 1
        if len(name) == 1:
            return [(name[0], 1)]
        
        for i in range(1, len(name)):
            if name[i] == name[i-1]:
                count += 1
                continue
            temp.append((name[i-1], count))
            count = 1
        if len(name) > 0:
            temp.append((name[i], count))
        return temp
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_consecutive_count = self.consecutieve_count(name)
        typed_consecutive_count = self.consecutieve_count(typed)

        if len(name_consecutive_count) != len(typed_consecutive_count):
            return False

        if len(name_consecutive_count) == len(typed_consecutive_count) == 0:
            return False
        
        for name_cons, typed_cons in zip(name_consecutive_count, typed_consecutive_count):
            if name_cons[0] != typed_cons[0]:
                return False
            if name_cons[1] > typed_cons[1]:
                return False
        return True



def main():
    s = Solution()
    print(s.isLongPressedName("a", "aaaaaaaaaaaaaaaaa"))

if __name__ == "__main__":
    main()