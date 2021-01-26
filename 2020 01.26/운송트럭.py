# 운송트럭
def solution(max_weight, specs, names):
    count = 1
    sum1 = 0
    my_dict = {}
    for index, truck in specs:
        my_dict[index] = truck
    for name in names:
        sum1 += my_dict[name]
        print(sum1)
        if sum1 <= max_weight:
            continue
    
        else:
            sum1=my_dict[name]
            count=count+1
    return count