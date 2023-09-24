import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

book = list(map(int, input().split()))

book.sort()

book = deque(book)

result = 0

minus = []
plus = []

max_v = 0
for i in book:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
    if abs(i) > max_v:
        max_v = abs(i)

if minus:
    for i in range(0, len(minus), M):
        result += (abs(minus[i]) * 2)
if plus:
    for i in range(len(plus)-1, -1, -M):
        result += (plus[i] * 2)
result -= max_v
print(result)
# -39 -37 -29 -28 -6 0 2 11

# -45 -26 -18 -9 -4 0 1 22 40 50

#-1 3 4 5 6 11