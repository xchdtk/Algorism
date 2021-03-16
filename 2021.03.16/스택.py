import sys

a_stack = list()
def push(X):
    a_stack.append(X)
def pop():
    if(size()==0):
        print(-1)
    else:    
        print(a_stack[-1])
        del a_stack[-1]
def size():
    return len(a_stack)
def empty():
    if size() ==0:
        print(1)
    else:
        print(0)
def top():
    if size() == 0:
        print(-1)
    else:
        print(a_stack[-1])
        
n= int(sys.stdin.readline())
        
for i in range(n):
    a=sys.stdin.readline().split()
    if(a[0]=='push'):
        push(a[1])
    elif(a[0]=='pop'):
        pop()
    elif(a[0]=='size'):
        b=size()
        print(b)
    elif(a[0]=='empty'):
        empty()
    elif(a[0]=='top'):
        top()