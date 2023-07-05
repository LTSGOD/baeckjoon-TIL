import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

듣 = sorted([input().rstrip() for _ in range(N)])

보 = sorted([input().rstrip() for _ in range(M)])

result = []

i = 0
j = 0
while i < N and j < M:
    if(듣[i] == 보[j]):
        result.append(듣[i])
        i += 1
        j += 1
    elif(듣[i] < 보[j]):
        i += 1
    else:
        j += 1
print(len(result))
[print(person) for person in result]
