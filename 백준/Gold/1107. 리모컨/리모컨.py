import sys
import math
input = sys.stdin.readline

N = int(input())

M = int(input())


if(M > 0):
    고장 = list(map(int, input().split()))
else:
    고장 = []

min1 = abs(N - 100)
for num in range(999999):
    num_list = list(map(int, str(num)))
    flag = False
    for button in 고장:
        if(button in num_list):
            flag = True
            break
    if(flag == True):
        continue

    tmp = len(num_list) + abs(N - num)
    if(tmp < min1):
        min1 = tmp

print(min1)
