from collections import deque
# bfs queue 이용


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    n = len(numbers)
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])

        else:
            if temp == target:
                answer += 1

    return answer
