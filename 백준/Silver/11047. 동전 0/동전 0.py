import sys
from math import sqrt

input = sys.stdin.readline

N,K = map(int, input().split())

value = []
for _ in range(N):
    value.append(int(input()))

value.sort(reverse=True)

result = 0
for v in value:
    tmp = K // v
    result += tmp
    K = K % v

print(result)