n      = int(input())
n_list = [0]
dp     = [0] * (n+1)
for number in range(n):
    num = int(input())
    n_list.append(num)

for index in range(1, len(n_list)):

    if index == 2:
        dp[index] = n_list[index-1] + n_list[index]
        continue
    
    dp[index] = max(dp[index-2] , dp[index-3] + n_list[index-1]) + n_list[index]

print(dp[-1])
