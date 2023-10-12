import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

#시간 복잡도 check
#20C10 ~ 1더한 것이 이 최악의 경우 1700000
# 제한시간 2초
# 조합 구해서 더한 다음 S되는 거 갯수 구하는 문제

N, S = map(int, input().split())

sequence = list(map(int, input().split()))
result = []

def recursion(depth, C, start):
    global count

    if depth == C:
        # print(result)
        if sum(result) == S:
            count+=1
        return

    for i in range(start, N):
       
        result.append(sequence[i])
        recursion(depth + 1, C, i + 1)
        result.pop()

count = 0
for i in range(1,N+1):
    recursion(0,i,0)
print(count)
