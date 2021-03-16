n       = int(input())
ox_list = []
stack   = []
count   = 1
status  = True

for number in range(n):
    num = int(input())
    
    while count <= num:
        ox_list.append("+")
        stack.append(count)
        count += 1

    if stack[-1] == num:
        stack.pop()
        ox_list.append('-')
    else:
        status = False

if not status:
    print("NO")
else:
    for i in ox_list:
        print(i)
    
