n, k  = list(map(int, input().split()))

coins = [int(input()) for number in range(n)]
coins.reverse()
count = 0

for coin in coins:
    if coin > k:
        continue

    count = count + k//coin
    k = k - (k//coin) * coin 
    

    if not k:
        break

print(count)