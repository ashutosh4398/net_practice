# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluate_expression(operator_int, left_val, right_val):
    if (operator_int == -1):
        return left_val + right_val
    elif operator_int == -2:
        return left_val - right_val
    elif operator_int == -3:
        return int(left_val / right_val)
    elif operator_int == -4:
        return left_val * right_val



def evaluateExpressionTree(tree):
    if tree.left is None and tree.right is None:
        return tree.value
    # Write your code here.
    left_value = evaluateExpressionTree(tree.left)
    operator = tree.value
    right_value = evaluateExpressionTree(tree.right)

    return evaluate_expression(operator, left_value, right_value)


