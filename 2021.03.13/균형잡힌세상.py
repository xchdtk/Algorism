while True:
    str_long = input()
    if str_long == ".":
        break
    check = True
    stack = []
    for i in str_long:
        if stack and i == ")":
            if stack[-1] == '(':
                stack.pop()
            elif stack [-1] == '[':
                check = False
                
                
        elif stack and i == ']':
            if stack[-1] == '[':
                stack.pop()
            
            elif stack[-1] == '(':
                check = False
        else:
            if i == '(' or i==")" or i == '[' or i==']':
                stack.append(i)
            
    
    if check == False or stack:
        print("no")
    else:
        print("yes")