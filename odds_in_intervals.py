"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # no_of_odds = 0

        # low_remaining = -low % 10
        # high_completed = high % 10

        # for i in range(low_remaining):
        #     if (low + i) % 2 == 1:
        #         no_of_odds += 1
        # for i in range(high_completed):
        #     if (high - i) % 2 == 1:
        #         no_of_odds += 1

        # low = low + low_remaining
        # high = high - high_completed

        # no_of_odds += ((high - low) // 10) * 5
        # return no_of_odds

        approx = (high - low) / 2
        return int(approx) if low % 2 == 0 and high % 2 == 0 else int(approx + 1)


def main():
    s = Solution()
    print(s.countOdds(2, 98))


if __name__ == "__main__":
    main()
