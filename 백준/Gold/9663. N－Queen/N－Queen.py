import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N = int(input())

def possible(coordinate):
    for q_x, q_y in enumerate(queen_pos):
        if q_y == -1:
            continue
        x = coordinate[0] - q_x
        y = coordinate[1] - q_y

        #대각선 조회
        if abs(x) == abs(y):
            return False
        # 양옆 위아래 조회
        if x == 0 or y == 0:
            return False
    return True

visited = [False] * N
queen_pos = [-1 for _ in range(N)]


def recursion(depth):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):

        #해당 열 방문 하지 않았으면
        if visited[i] == False:
            

            if possible((depth, i)):
                visited[i] = True
                queen_pos[depth] = i
                recursion(depth+1)
                visited[i] = False
                queen_pos[depth] = -1

result = 0
recursion(0)
print(result)


#possible에서 전단계에 모든 퀸에 대한 가능성을 검사 -> 이것이 시간초과 유발?
# def possible(coordinate, queen_pos):
#     for q_x, q_y in queen_pos:
#         if q_y == -1:
#             continue
#         x = coordinate[0] - q_x
#         y = coordinate[1] - q_y

#         #대각선 조회
#         if abs(x) == abs(y):
#             return False
#         # 양옆 위아래 조회
#         if x == 0 or y == 0:
#             return False
#     return True

# def recursion(depth, queen_pos):
#     global count
#     # print("----------------")
#     if depth == N:
#         count += 1
#         return

#     for i in range(N):
#         #해당 자리가 놓을 수 있는 자리라면
#         if possible((depth, i), queen_pos):
#             # print(f'{depth, i}')
            
#             #가능한 자리면 퀸의 좌표 추가
#             queen_pos_copy = deepcopy(queen_pos)
#             queen_pos_copy.append((depth, i))
#             # print(queen_pos_copy)
#             recursion(depth+1, queen_pos_copy)
#     return

# count = 0

# recursion(0, deque())
# print(count)