import math
n = int(input())
for number in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    equation = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if not equation and r1 == r2:
        print(-1)
    elif (r1+r2) == equation or abs(r1-r2) == equation:
        print(1)
    elif abs(r1 - r2) < equation < (r1 + r2):
        print(2)

    else:
        print(0)
