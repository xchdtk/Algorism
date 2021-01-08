# 배상비용최소화
import heapq
def solution(no, works):
    heap_1 =[]
    for worksid in works:
        heapq.heappush(heap_1,(-worksid,worksid))
        
    while no != 0:
        tmp = heapq.heappop(heap_1)[1]-1
        heapq.heappush(heap_1,(-tmp,tmp))
        no = no - 1
    result = 0 
    while heap_1:
        a = heapq.heappop(heap_1)[1]

        if a <= 0:
            continue
        else:
            result += a * a
        
    return result