def solution(s):
    stack = []
    for chracter in s:
        if stack and stack[-1] == chracter:
            stack.pop()
            continue
        stack.append(chracter)

    if stack:
        return 0
    return 1
