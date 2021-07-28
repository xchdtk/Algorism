def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

n = int(input())
for i in range(n):
    n1, n2 = map(int, input().split())
    a = gcd(max(n1, n2), min(n1,n2))
    print(n1*n2//a)