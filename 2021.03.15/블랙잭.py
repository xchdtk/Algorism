n,m = map(int, input().split())
n_list = list(map(int, input().split()))
target = 0

for i in range(len(n_list)):
    for j in range(i+1, len(n_list)):
        for p in range(j+1, len(n_list)):
            if n_list[i] + n_list[j] + n_list[p] <= m:
                if target < n_list[i] + n_list[j] + n_list[p]:
                    target = n_list[i] + n_list[j] + n_list[p]

print(target)