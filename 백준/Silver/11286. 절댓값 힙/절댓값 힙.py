import sys
import heapq

input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    tmp = int(input())
    if(tmp != 0):
        heapq.heappush(queue, (abs(tmp), tmp))
    else:
        if queue:
            result = heapq.heappop(queue)
            print(result[1])
        else:
            print(0)
