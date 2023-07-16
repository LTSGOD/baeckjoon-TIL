import sys
import heapq

input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    tmp = int(input())
    if(tmp > 0):
        heapq.heappush(queue, -tmp)
    else:
        if queue:
            result = heapq.heappop(queue)
            print(-result)
        else:
            print(0)
