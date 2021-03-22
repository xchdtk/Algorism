n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for number in range(3, n+1):
    dp[number] = (dp[number-2] + dp[number-1]) % 15746

print(dp[n])