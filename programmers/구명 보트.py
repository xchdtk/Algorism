def solution(people, limit):
    people.sort()
    count = 0
    start, end = 0, len(people)-1

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        count += 1

    return count
