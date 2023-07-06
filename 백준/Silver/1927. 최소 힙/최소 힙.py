import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

result = []
for _ in range(N):
    tmp = int(input())

    if(tmp > 0):
        heappush(result, tmp)
    else:
        if result:
            print(heappop(result))
        else:
            print(0)
