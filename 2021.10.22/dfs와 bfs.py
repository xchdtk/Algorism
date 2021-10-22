# dfs
# 시간 복잡도
# 노드 수: V
# 간선 수: E
# 시간 복잡도: O(V + E)
from sys import stdin
from collections import deque

N, M, start = map(int, stdin.readline().split())
graph = [[0]*(N+1) for i in range(N+1)]

for number in range(M):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = graph[y][x] = 1


def dfs(start):
    visited = []
    stack = [start]
    while stack:
        pop = stack.pop()
        if str(pop) not in visited:
            str_pop = str(pop)
            visited.append(str_pop)
            for number in range(N, -1, -1):
                if graph[pop][number] == 1:
                    stack.append(number)

    return ' '.join(visited)

def bfs(start):
    visited = []
    queue = deque([start])
    while queue:
        pop = queue.popleft()
        if str(pop) not in visited:
            str_pop = str(pop)
            visited.append(str_pop)
            for number in range(1, N+1):
                if graph[pop][number] == 1:
                    queue.append(number)

    return ' '.join(visited)

print(dfs(start))
print(bfs(start))

        
    
