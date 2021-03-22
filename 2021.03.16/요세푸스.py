from collections import deque
a1 = deque([])
n, k = map(int,input().split()) 
for i in range(1,n+1):
    a1.append(i)
print('<',end = "")
for i in range(4):
    for j in range(k-1):
        a1.append(a1[0])
    pop = a1.popleft()
    print(pop, end='')

    
print('>')