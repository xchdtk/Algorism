def solution(brown, yellow):
    total = brown + yellow
    for vertical in range(1, total+1):
        if not total % vertical:
            width = total / vertical
            if width >= vertical:
                print(width, vertical)
                print((2*width) + (2*vertical))
                if (2*width) + (2*vertical) == brown + 4:
                    print(width, vertical)
                    return [width, vertical]


brown = 8
yellow = 1
print(solution(brown, yellow))
