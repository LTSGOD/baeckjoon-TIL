import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

array = deque(map(int, input().split()))

array.appendleft(0)

mid = len(array)//2

result = deque()
i = 1
j = 2
while i <= mid:
    tmp = []
    for index in range(i, len(array), j):
        tmp.append(array[index])
    j *= 2
    i *= 2
    result.appendleft(tmp)

for l in result:
    for s in l:
        print(s,end=" ")
    print()