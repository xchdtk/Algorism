# 기능개발
import math
from collections import deque
def solution(progresses, speeds):
    qu = deque()
    for index in range(len(progresses)):
        qu.append(int(math.ceil((100-progresses[index])/speeds[index])))
    print(qu)

    result = []
    count, deloy  = 1,qu.popleft()
    
    while qu:
        deloy_1 = qu.popleft()
        if deloy >= deloy_1:
            count = count+1
            
        else:
            result.append(count)
            count = 1
            deloy = deloy_1

        
    result.append(count)
    
    return result