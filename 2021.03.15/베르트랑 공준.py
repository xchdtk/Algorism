import sys

is_prime    = [1] * 246913

is_prime[0] = 0
is_prime[1] = 0

sosu = []

for i in range(2, 246913):
    if is_prime[i]: 
        for j in range(i * i, 246913, i):
            is_prime[j] = 0

while True:
    number = int(sys.stdin.readline())
    
    if not number: 
        break
    print(sum(is_prime[number+1:2*number+1]))
    