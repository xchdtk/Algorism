N          = int(input())
paper_list = []
blue       = 0
white      = 0
for _ in range(N):
    paper_list.append(list(map(int, input().split())))


def paper_test(x,y,n):
    global blue, white, paper_list
    first_color = paper_list[y][x]
    status = False

    for i in range(x, x+n):
        if status:
            break

        for j in range(y, y+n):
            if first_color != paper_list[j][i]:
                paper_test(x, y, n//2) # 2사분면
                paper_test(x+n//2, y, n//2) # 1사분면
                paper_test(x, y+n//2, n//2) # 3사분면
                paper_test(x+n//2, y+n//2, n//2) # 4사분면
                status = True
                break
        
    if not status:
        if paper_list[y][x] == 1:
            blue += 1

        else:
            white += 1

paper_test(0,0,N)
print(white)
print(blue)


