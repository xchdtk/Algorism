a,b= input().split()
a=int(a)
b=int(b)

if b>=45:
    b=b-45
elif b<45:
    if a== 0:
        a=23
    else:    
        a=a-1
    b=b+15

print(a,b)