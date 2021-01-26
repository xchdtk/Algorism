# 전염병
def valid(next_x,next_y,n,m):
        return 0 <= next_x < m and 0 <= next_y < n

def solution(m,n,infests, vaccinateds):
    infection = []
    answer = 0
    remainder = []
    days = 0
    index = 0
    count = m*n
    visited = [[False] * n for j in range(m)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for vaccinatedsed in vaccinateds:
        a,b = vaccinatedsed
        visited[a-1][b-1] = True
        count = count-1

    for infestsed in infests:
        a,b = infestsed
        visited[a-1][b-1] = True
        infection.append([a-1,b-1,days])
        count = count-1
    
    while count > 0 and infection:
        remainder.append(infection.pop(0))
        print(answer)
        for i in range(4):
            next_x = dx[i] + remainder[0][0]
            next_y = dy[i] + remainder[0][1]
            if not valid(next_x,next_y,n,m) or visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            count = count - 1
            answer = remainder[0][2] + 1
            infection.append([next_x,next_y,remainder[0][2]+1])
        remainder.clear()
    if count <= 0:
        return answer
    return -1

    


        
    

