# 더 맵게
import heapq
from collections import deque
def solution(scoville,k):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2 and scoville[0] < k:
        heap_1 = heapq.heappop(scoville)
        heap_2 = heapq.heappop(scoville)
        heapq.heappush(scoville,heap_1+(heap_2*2))
        count = count + 1
        
    if scoville[0] >= k:
        return count
    else:
        return -1
    
scoville = [1,2,3,9,10,12]
k = 7
print(solution(scoville,k))