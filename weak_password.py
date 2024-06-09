"""
2299. Strong Password Checker II
Easy
Topics
Companies
Hint
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.
"""

import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        patterns = ["[A-Z]", "[a-z]", "[0-9]", "[!@#$%^&*()\-+]"]
        for pattern in patterns:
            if not re.findall(pattern, password):
                return False

        for idx in range(1, len(password[1:])):
            if password[idx - 1] == password[idx]:
                return False

        return True


def main():
    s = Solution()
    print(s.strongPasswordCheckerII("-Aa1a1a1"))


if __name__ == "__main__":
    main()
