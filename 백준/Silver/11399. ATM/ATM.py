import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

times = sorted(list(map(int, input().split())))

result = []

tmp = 0
for time in times:
    tmp += time
    result.append(tmp)

print(sum(result))
