size  = int(input())
numbers   = list(map(int, input().split()))

count = 1
max_number = 0
for number in range(len(numbers)):
    if number == 0:
        max_number = numbers[number]
        continue

    if numbers[number] > max_number:
        max_number = numbers[number]
        count += 1

print(count)
