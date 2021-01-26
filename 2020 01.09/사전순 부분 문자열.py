# 사전순 부분 문자열
def solution(s):
    stack = []
    for string in s:
        while stack and ord(stack[-1]) < ord(string):
            stack.pop()
        stack.append(string)
    str_1 = "".join(stack)
    return str_1
        
    
    
