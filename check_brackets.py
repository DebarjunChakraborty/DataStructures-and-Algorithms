def check_brackets(s):
    stack = []
    bracket_map={')': '(', ']': '[', '}': '{'}
    bracket_pos={'(': [], '[': [], '{': []}
    for i, char in enumerate(s):
        if char in "([{":
            stack.append(char)
            bracket_pos[char].append(i)
        elif char in ")]}":
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
                bracket_pos[bracket_map[char]].pop()
            else:
                return i + 1
    if stack:
        return bracket_pos[stack[-1]][0] + 1
    return "success"
s = input().strip()
print(check_brackets(s))