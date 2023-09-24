import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    max = 0
    result = 0
    #바로 최댓값 구하고 result 에 계속 더해줌
    for i in range(len(stock)-1, -1, -1):
        if stock[i] > max:
            max = stock[i]
        result += (max - stock[i])
    print(result)
    