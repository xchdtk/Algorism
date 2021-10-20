def solution(prices):
    answer = []
    for index1 in range(len(prices)):
        count = 0
        for index2 in range(index1+1, len(prices)):
            if prices[index1] <= prices[index2]:
                count += 1
                continue
        answer.append(count)
        
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
