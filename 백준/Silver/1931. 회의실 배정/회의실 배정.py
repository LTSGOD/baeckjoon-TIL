import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

time_table = [list(map(int, input().split())) for _ in range(N)]

time_table = sorted(time_table, key=lambda x: (x[1], x[0]))

i = 1
count = 1
endtime = time_table[0][1]
while i < N:
    if(time_table[i][0] >= endtime):
        count += 1
        endtime = time_table[i][1]
    i += 1
print(count)