import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y):

    q = deque()
    q.append((x, y))

    while(q):
        current_x, current_y = q.popleft()

        if visited[current_x][current_y] == True:
            continue
        visited[current_x][current_y] = True

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_x = current_x + dx
            next_y = current_y + dy
            if(next_x < 0 or next_x > n - 1 or next_y < 0 or next_y > m - 1):
                continue
            if(board[next_x][next_y] == 0):
                continue
            if(visited[next_x][next_y] == False):
                board[next_x][next_y] = board[current_x][current_y] + 1
            q.append((next_x, next_y))


visited = [[False] * m for _ in range(n)]

flag = False
for i in range(n):
    for j in range(m):
        if(board[i][j] == 2):
            board[i][j] = 0
            bfs(i, j)
            flag = True
            break
    if(flag == True):
        break

for i in range(n):
    for j in range(m):
        if(board[i][j] == 1 and visited[i][j] == False):
            board[i][j] = -1

for i in board:
    for j in i:
        print(j, end=" ")
    print()
