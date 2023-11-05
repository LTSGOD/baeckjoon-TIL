import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline


#일단 노가다로 모든 경우를 가정해서 풀면 최대 7P7(타선뽑기) * 50(이닝수계산) * 최대타수(27 1명만 아웃될때)
# 54432000 으로 브루트 포스 가능할듯?
# 1. base 점수 세는 거 고침
# 2. 다음 타자 번호 if문 제거
# 3. score 점수 매기는거 boolean 에서 정수로 변경
# 4. insert 연산이 오래걸리는 것같아서 변경
# 5. map 연산 변경 -> 상관ㅇ없음
# 6. 계속 꺼내지 말고 한번 만 꺼내서 확인
# 7. sum(함수 생략)

# 순열 구현
def permutation(depth):

    if depth == 8:
        hitter_order.append([*result])
        return

    for i in range(2,10):

        if visited[i]:
            continue

        result.append(i)
        visited[i] = True
        permutation(depth+1)
        visited[i] = False
        result.pop()
visited = [False for _ in range(10)]

#타순 모든 경우의 수 구하기
hitter_order = []

result = []

permutation(0)

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

max_score = -1


#가능한 모든 타순 계산
for player_list in hitter_order:

    score = 0

    #1번타자 추가
    player_list = list(player_list[:3]) + [1] + list(player_list[3:])

    현재타자 = 0

    #게임 시작
    for 한이닝_득점정보 in info:

        #아웃카운트와 베이스는 이닝마다 초기화
        out = 0
        base = [0,0,0]

        
        while out < 3:

            hit = 한이닝_득점정보[player_list[현재타자]-1]
            
            #타순에 따라 한이닝득점정보에 따라 계산
            if hit == 0:
                out += 1
            elif hit == 1:
                score += base[2]
                base = [1, base[0], base[1]]
            elif hit == 2:
                score += base[1] + base[2]
                base = [0, 1, base[0]]
            elif hit == 3:
                score += base[0] + base[1] + base[2]
                base = [0, 0, 1]
            elif hit == 4:
                score += base[0] + base[1] + base[2]  + 1
                base = [0,0,0]
            
            #최적화
            현재타자 += 1

            if 현재타자 > 8:
                현재타자 = 0

    #최댓값 갱신 
    if score > max_score:
        max_score = score

print(max_score)
