number     = int(input())
connect    = int(input())
graph = [[0]*(number+1) for _ in range(number+1)]
virus = []
stack = []
for _ in range(connect): 
    x, y = map(int, input().split()) 
    graph[x][y], graph[y][x] = 1, 1


def dfs(x): 
    stack.append(x)
    while stack:
        pop = stack.pop()
        if pop not in virus:
            virus.append(pop)
            for num in range(1, number + 1):
                if graph[pop][num] == 1 and num not in virus:
                    stack.append(num)
    return len(virus) - 1
            

print(dfs(1))

