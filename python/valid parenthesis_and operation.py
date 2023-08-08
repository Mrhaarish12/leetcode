"""
Getting an input string s and adding the minimum number of parenthesis and in any positon so that the resulting parentheses string is valid.

"""

x = "'(' and ')'"
s = input(f"Enter the input parenthesis string {x}: ")
stack, min_add = [], 0
for char in s:
    if char in ('('):
        stack.append(char)
    else:
        if not stack:
            min_add += 1
            continue
        popped = stack.pop()
        if char == ')' and popped != '(':
            min_add += 1
            continue
min_add += len(stack)
print(f"Minimum numbr of parameters we must add to make the resulting string valid: {min_add}")