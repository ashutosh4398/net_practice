# "()[]{(hhh)}"
# ([{}])

expression = "()"
closing_brackets = {")": "(", "]": "[", "}": "{"}
opening_brackets = {"(": ")", "[": "]", "{": "}"}

is_valid = True
for i,char in enumerate(expression):
    if char in closing_brackets:
        matching_bracket = closing_brackets[char]
        start, end, diff = i-1, -1, -1
    elif char in opening_brackets:
        matching_bracket = opening_brackets[char]
        start, end, diff = i+1, len(expression), 1
    else:
        continue

    is_valid = False
    for j in range(start, end, diff):
        if expression[j] == matching_bracket:
            is_valid = True
            break

    if not is_valid:
        break
    

print(is_valid)
