"""
20. Valid Parentheses.
"""
BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def is_valid(s):
    stack = []

    for i in s:

        if i in BRACKETS:
            stack.append(i)

        else:
            # Проверка на пустой стек и соответствие
            if not stack or BRACKETS[stack[-1]] != i:
                return False
            stack.pop()  # Убираем последнюю открывающую скобку

    return not stack


s = '(([]))'

print(is_valid(s))

# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true
