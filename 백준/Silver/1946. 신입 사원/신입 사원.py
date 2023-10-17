import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    newbie = []

    #newbie들 입력 받기
    for _ in range(N):
        a,b = map(int, input().split())
        newbie.append((a,b))
    
    #newbie들 1등부터 정렬
    newbie.sort()

    #standard에 가장 큰 수 넣기
    standard = int(1e9)
    result = 0
    # 드가보자
    for score1, score2 in newbie:

        #만약 standard보다 score2 순위가 낮다면 합격! 
        #그리고 그 수가 다시 기준이 됨. 유사 DP 같은 느낌
        #예시
        # 1 5
        # 2 4
        # 3 8
        # 4 7
        # 5 1
        # 6 3
        # 7 2
        # 8 6
        if score2 < standard:
            standard = score2
            result += 1
    print(result)
