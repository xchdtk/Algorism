def next_max_number(number): 
    len_one = 0
    max_number = 79
    for n in range(1):
        new_number = 78
        stack = []
        count= 0
        while new_number != 1 or new_number != 0:
            count += 1
            share     = new_number // 2
            remainder = new_number % 2

            print(new_number)
            print(share)
            print(remainder)
            print(stack)

            new_number = share
            if remainder:
                stack.append(remainder)

            if count == 10:
                return
        if new_number:
            stack.append(new_number)
        return len_one

number = 78
print(next_max_number(number))


            
            



