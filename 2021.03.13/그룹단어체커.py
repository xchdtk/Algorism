n     = int(input())
stack = []
count = 0
status = True
for number in range(n):
    word = input()
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])

        if stack and stack[-1] != word[i]:
            if word[i] in stack:
                status = False 
                continue
            stack.append(word[i])
            
    if status:
        count += 1
    
    stack  = []
    status = True
print(count)
        
    

        

