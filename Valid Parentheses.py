def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}  # Matching pairs

    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            top = stack.pop() if stack else '#'  # Get last open bracket
            if top != bracket_map[char]:  # Check if it matches
                return False
        else:
            stack.append(char)  # Push open brackets to stack

    return not stack  # If stack is empty, it's valid

print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))