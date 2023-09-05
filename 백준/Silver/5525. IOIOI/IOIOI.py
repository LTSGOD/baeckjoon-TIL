import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

P = input().rstrip()

i = 0
count = 0
result = 0
while i < M - 2:
    if P[i:i+3] == "IOI":
        count +=1
        i += 2
        if count == N:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)