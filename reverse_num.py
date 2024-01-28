class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)
        reverse = 0
        while x != 0:
            # here we have divided the max and min int because
            # in next steps we are multiplying our reverse with 10
            # thus to check if the multiplication might cause overflow or not
            if reverse < MIN_INT/10 or reverse > MAX_INT/10:
                return 0
            digit = x%10 if x > 0 else x%-10
            reverse = reverse * 10 + digit
            x = int(x/10)
        return reverse

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123))