from collections import deque
n = int(input())
n_list = deque([num for num in range(1, n+1)])
while len(n_list) > 1:
    high = n_list.popleft()
    n_list.append(n_list.popleft())

print(n_list[0])