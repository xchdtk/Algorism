a = int(input())
for i in range(a):
    b = input()
    sum = 0
    for i in b:
        if i == '(':
            sum += 1
            continue
        sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')