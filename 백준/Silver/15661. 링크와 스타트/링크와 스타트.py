import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N = int(input())

competence = []

for _ in range(N):
    competence.append(list(map(int, input().split())))

member_num = 0

member = [i for i in range(N)]
min = int(1e8)

for member_num in range(2,N//2+1):
    tmp = combinations(member, member_num)
    #조합마다 차이 구함.
    for comb in tmp:
        
        start = 0
        link = 0

        #각 멤버별로 계산
        for k in member:
            #스타트팀 능력치 구하기
            if k in comb:
                for l in comb:
                    start += competence[k][l]
            #링크 팀 능력치 구하기
            else:
                for j in member:
                    #스타트 팀이면 패스
                    if j in comb:
                        continue
                    link += competence[k][j]
        if  abs(start-link) < min:
            min = abs(start-link)
    #     print(comb)
    #     print(min)
    # print(min)
    # break
print(min)