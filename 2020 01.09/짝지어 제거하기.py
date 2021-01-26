# 짝지어 제거하기
def solution(s):
    stack = list(s[0])
    counter = 0
    for move in s[1:]:
        if stack and stack[-1] == move:
            stack.pop()
        else:
            stack.append(move)
        
          
    if stack:
        return 0
    return 1
