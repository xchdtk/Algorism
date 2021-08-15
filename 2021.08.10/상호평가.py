def solution(scores):
    max_score = []
    min_score = []
    result    = []
    same      = []
    n = len(scores)
    for i in range(n):
        for j in range(n):
            if i == j:
                same.append(scores[i][j])
            if len(max_score) == j:
                max_score.append(scores[i][j])

            if len(min_score) == j:
                min_score.append(scores[i][j])

            if len(result) == j:
                result.append([scores[i][j]])
                continue
            
            if max_score[j] < scores[i][j]:
                max_score[j] = scores[i][j]

            if min_score[j] > scores[i][j]:
                min_score[j] = scores[i][j]
            result[j].append(scores[i][j])

    return max_score, min_score, result

scores = [
    [100, 90, 98, 88, 65], 
    [50, 45, 99, 85, 77],
    [47, 88, 95, 80, 67], 
    [61, 57, 100, 80, 65], 
    [24, 90, 94, 75, 65]
    ]

print(solution(scores))


