import sys

r = sys.stdin.readline

n           = int(input())
graph       = [list(map(int,r().strip())) for _ in range(n)]
visited     = [[0] * n for _ in range(n)] 
check_count = []
stack       = []
count       = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x,y, count):
    stack.append([x, y])
    visited[x][y] = 1
    count         += 1
    while stack:

        pop = stack.pop()
        x = pop[0]
        y = pop[1]
        
        for index in range(4):
            new_x = x + dx[index]
            new_y = y + dy[index]
            
            if 0 <= new_x < n  and 0 <= new_y < n and visited[new_x][new_y] == 0 and graph[new_x][new_y] == 1:
                visited[new_x][new_y] = 1
                stack.append([new_x,new_y])
                count += 1
    return count

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1 and not visited[i][j]:
            check_count.append(dfs(i,j,count))

print(len(check_count))
for i in sorted(check_count):
    print(i)