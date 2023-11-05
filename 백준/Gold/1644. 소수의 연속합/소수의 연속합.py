import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

N = int(input())

#소수로 나누어 지면 소수 아님
#규칙 일단 소수를 쭉구하는데 모두 구하면 시간초과
#따라서 소수를 더해가며 N이 넘는 범위에서 멈추고
#반례 그 범위 이상에서 더해도 값이 나올 수있다.
#소수를 빠르게 구하지 못해서 위 방법을 생각했는데 더 빨리 구하는 방법이 존재
# 노가다로 구했는데 소수를 구하면 그 배수를 다 체크해주는식으로

소수 = [False, False] + [True] * (N-1)

for i in range(2, N+1):

    if 소수[i]:
        for j in range(i*2, N+1, i):
            소수[j] = False
    
count = 0
for i in range(2, len(소수)):
    if not 소수[i]:
        continue

    sum = i
    if sum == N:
        count +=1
    for j in range(i+1,len(소수)):
        if not 소수[j]:
            continue
        sum += j

        if sum > N:
            break
        if sum == N:
            count +=1
            break

print(count)
