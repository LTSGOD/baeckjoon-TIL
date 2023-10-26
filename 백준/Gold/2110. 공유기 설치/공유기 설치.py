import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


N, C = map(int, input().split())

location = []

for _ in range(N):
    location.append(int(input()))

location.sort()

start = 1
end = location[-1] - location[0]

def check(mid):
    기준 = location[0]
    count = 1

    for i, n in enumerate(location):
        if i ==0:
            continue

        #기준노드로부터 mid이상 떨어져있다면
        if n - 기준 >= mid:
            기준 = n
            count += 1
    
    #공유기가 적거나 같으면 True
    if count >= C:
        return True
    #공유기가 많으면 False
    else:
        return False

while start+1 < end:

    #공유기 간격을 4이상 뒀을 때
    mid = (start+end)//2

    #공유기가 적다 -> 간격을 넓혀서 더 설치 가능
    if check(mid):
        start = mid
    else:
        end = mid


#예외 발생
#1 10
#경우 start만 출력시 8출력
if end == location[-1] - location[0]:
    print(end)
else:
    print(start)

