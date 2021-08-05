def solution(price, money, count):
    sum_fee = 0
    for number in range(1, count+1):
        sum_fee += number * price

    if money > sum_fee:
        return 0
    return sum_fee - money


price = 3
money = 20
count = 4
print(solution(price, money, count))
