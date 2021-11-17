def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    answer = n - len(set_lost)
    for student in set_reserve:
        if student - 1 in set_lost:
            set_lost.remove(student-1)
            answer += 1

        elif student + 1 in set_lost:
            set_lost.remove(student+1)
            answer += 1

    return answer


lost = [2,3,4]
reserve = [1,2,3]
print(solution(5, lost, reserve))
