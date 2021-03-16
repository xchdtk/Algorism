from collections import deque
a1 = deque([])
n, k = map(int,input().split()) 
for i in range(1,n+1):
    a1.append(i)
print('<',end = "")
while a1:
    for j in range(k-1):
        a1.append(a1[0])
        a1.popleft()

    print(a1.popleft(),end="")
    if a1:
        print(', ',sep='',end="")
print('>')