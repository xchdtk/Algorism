n = int(input())

decomposition = [i for i in range(0, 1000001)]
part_sum = 0
for number in range(len(decomposition)):
    str_number = str(decomposition[number])
    part_sum = 0
    for num in str_number:
        part_sum += int(num) 
 
    decomposition[number] = part_sum + decomposition[number]
    if number == n:
        print(0)
        break

    if decomposition[number] == n:
        print(number)
        break

    


    