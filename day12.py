def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs.get(char):
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid("()"))
print(is_valid("([)]"))
print(is_valid("[{()}]"))
print(is_valid(""))
print(is_valid("{[}"))
