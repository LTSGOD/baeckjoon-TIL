import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

tmp = 0

num_l = [0]
for num in list(map(int, input().split())):
    num_l.append(tmp + num)
    tmp += num


for _ in range(M):
    start, end = map(int, input().split())
    print(num_l[end]-num_l[start-1])
