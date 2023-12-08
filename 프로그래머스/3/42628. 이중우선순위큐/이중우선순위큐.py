from collections import deque
from heapq import heappop, heappush

def solution(operations):
    
    최대큐 = []
    최소큐 = []

    operations = [i.split() for i in operations]
    for 명령, 숫자 in operations:
        if 명령=="I":
            heappush(최소큐, int(숫자))
            heappush(최대큐, -int(숫자))
        elif 명령 =="D" and 숫자 == "1":
            if 최대큐:
                tmp = heappop(최대큐)
                최소큐.remove(-tmp)
        else:
            if 최소큐:
                tmp = heappop(최소큐)
                최대큐.remove(-tmp)
    
    if 최소큐 and 최대큐:
        return [-heappop(최대큐), heappop(최소큐)]
    else:
        return [0,0]