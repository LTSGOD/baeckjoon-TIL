import sys
from collections import deque

input = sys.stdin.readline

#일단 좌표가 뒤집혀져서 받기 때문에 x,y 를 다 바꿔서 대칭해줌.
# 그후 dfs 탐색
N, M, K = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    y1,x1, y2, x2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = -1

def dfs(x, y):
    stack = deque()

    stack.append((x,y))
    count = 0
    while stack:
        current_x, current_y = stack.pop()

        if visited[current_x][current_y]:
            continue

        visited[current_x][current_y] = True
        count += 1

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            next_x = current_x + dx
            next_y = current_y + dy

            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1:
                continue
            if board[next_x][next_y] == -1:
                continue
            stack.append((next_x,next_y))

    return count
result = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and board[i][j] != -1:
            result.append(dfs(i,j))

result.sort()
print(len(result))

for r in result:
    print(r,end=" ")

# for i in board:
#     print(i)



