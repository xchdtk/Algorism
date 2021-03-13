from math import ceil
number = list(map(int, input().split()))
print(ceil((number[2] - number[0]) / (number[0] - number[1])) + 1)

 
