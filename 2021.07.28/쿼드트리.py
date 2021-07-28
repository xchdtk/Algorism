import sys
r = sys.stdin.readline

n = int(input())
quad_tree = [list(r().strip()) for _ in range(n)]

def compression(x, y, n):
    global result
    first_number = quad_tree[y][x]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if quad_tree[j][i] != first_number:
                result += '('
                compression(x, y, n//2) 
                compression(x+n//2, y, n//2) 
                compression(x, y+n//2, n//2) 
                compression(x+n//2, y+n//2, n//2) 
                result += ')'
                return
    result += quad_tree[y][x]

result = ''
compression(0,0,n)
print(result)

