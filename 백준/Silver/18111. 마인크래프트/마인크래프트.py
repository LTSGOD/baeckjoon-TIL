import sys
import math
input = sys.stdin.readline


N, M, B = map(int, input().split())

land = [list(map(int, input().split()))for _ in range(N)]

m = 0
for raw in land:
    tmp = max(raw)
    if(m < tmp):
        m = tmp

result = 1000000000000000
height = 0
for i in range(m + 1):
    m = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if(land[j][k] < i):
                min += (i - land[j][k])
            else:
                m += (land[j][k] - i)
    if(m + B < min):
        continue
    time = m * 2 + min
    if(time <= result):
        result = time
        height = i
print(result, height)
# 1. 블럭을 가져가는것으로 끝낼수있는가? 2. 그럴수없다면 블럭을 가져다놓는것만으로 끝낼수있나?
