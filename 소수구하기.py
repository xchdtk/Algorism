def sieve(m, n):
    is_prime    = [True] * (n+1)
    
    is_prime[0] = False
    is_prime[1] = False

    sosu = []

    for i in range(2, n+1):
        if is_prime[i] and m <= i:
            sosu.append(i)
        for j in range(i * i, n+1, i):
            is_prime[j] = False
    return sosu
        
numbers = list(map(int, input().split()))
for i in sieve(numbers[0], numbers[1]):
    print(i)

