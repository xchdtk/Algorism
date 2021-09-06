def next_max_number(number): 
    pass
    max_number = 1000001
    for n in range(number, max_number):
        new_number = n
        stack = []
        while new_number != 1 or new_number != 0:
            share     = new_number // 2
            remainder = new_number % 2

            new_number = share
            if remainder:
                stack.append(remainder)


            
            



