import sys
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

[print(i) for i in n_list]





