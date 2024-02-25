"""
You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

 

Example 1:

Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
It can be shown that 170 is the smallest possible value.
Example 2:

Input: expression = "12+34"
Output: "1(2+3)4"
Explanation: The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.
Example 3:

Input: expression = "999+999"
Output: "(999+999)"
Explanation: The expression evaluates to 999 + 999 = 1998.
 

Constraints:

3 <= expression.length <= 10
expression consists of digits from '1' to '9' and '+'.
expression starts and ends with digits.
expression contains exactly one '+'.
The original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

"""

class Solution:

    def evaluate(self, expression): 
        opening, closing = expression.index("("), expression.index(")")
        middle_expression = expression[opening+1: closing].split("+")
        middle_result = int(middle_expression[0]) + int(middle_expression[1])
        result = int(expression[:opening] or 1) * middle_result * (int(expression[closing+1:] or 1))
        return result
    
    def create_expression(self, left, right, num1, num2):
        left_exp = right_exp = ""
        if left < len(num1):
            left_exp = f"{num1[:left]}({num1[left:]}"
        if right >= 0:
            right_exp = f"{num2[:right+1]}){num2[right+1:]}"
        return left_exp, right_exp

    def minimizeResult(self, expression: str) -> str:
        num1, num2 = (x.strip() for x in expression.split("+"))
        left, right = 0, len(num2)-1
        minimal_val = int(num1) + int(num2)
        minimal_expression = f"({num1}+{num2})"
        left_exp, right_exp = f"({num1}", f"{num2})"
        # left skew
        while left < len(num1):
            left_exp_temp, right_exp_temp = self.create_expression(left, right, num1, num2)
            left_exp = left_exp_temp or left_exp
            right_exp = right_exp_temp or right_exp
            expression = f"{left_exp}+{right_exp}"
            value = self.evaluate(expression)
            if value < minimal_val:
                minimal_val = value
                minimal_expression = expression
            left += 1
        
        left, right = 0, len(num2)-1
        # right skew
        while right >= 0:
            left_exp_temp, right_exp_temp = self.create_expression(left, right, num1, num2)
            left_exp = left_exp_temp or left_exp
            right_exp = right_exp_temp or right_exp
            expression = f"{left_exp}+{right_exp}"
            value = self.evaluate(expression)
            if value < minimal_val:
                minimal_val = value
                minimal_expression = expression
            right -= 1
        left, right = 0, len(num2)-1

        # combination
        while left < len(num1) or right >= 0:
            for params in [(left+1, right), (left, right-1), (left+1, right-1)]:
                left_exp_temp, right_exp_temp = self.create_expression(*params, num1, num2)
                left_exp = left_exp_temp or left_exp
                right_exp = right_exp_temp or right_exp
                expression = f"{left_exp}+{right_exp}"
                value = self.evaluate(expression)
                print(expression, value)
                if value < minimal_val:
                    minimal_val = value
                    minimal_expression = expression
            left += 1
            right -= 1
        return minimal_expression

s = Solution()
print(s.minimizeResult("1155+7881"))
            


