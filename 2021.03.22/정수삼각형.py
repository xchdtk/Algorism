n        = int(input())

triangle= [list(map(int, input().split())) for number in range(n)]

for number in range(1, len(triangle)):
    for i in range(len(triangle[number])):
        if not i:
            triangle[number][i] = triangle[number][i] + triangle[number-1][i]
            continue

        if i == len(triangle[number])-1:
            triangle[number][i] = triangle[number][i] + triangle[number-1][i-1]
            continue

        triangle[number][i] = triangle[number][i] + max(triangle[number-1][i-1], triangle[number-1][i])
print(max(triangle[-1]))