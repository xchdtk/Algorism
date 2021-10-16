import math

def solution(progresses, speeds):
    count  = 1
    target = math.ceil((100 - progresses[0]) / speeds[0])
    answer = []

    for index in range(1, len(progresses)):
        number = math.ceil((100 - progresses[index]) / speeds[index])
        
        if number <= target:
            count += 1
            continue

        answer.append(count)
        target = number
        count = 1

    answer.append(count)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
            

