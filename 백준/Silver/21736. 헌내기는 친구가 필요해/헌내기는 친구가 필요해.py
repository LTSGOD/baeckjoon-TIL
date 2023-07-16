import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0
    while q:
        current_x, current_y = q.popleft()

        if(visited[current_x][current_y] == True):
            continue
        if(board[current_x][current_y] == 'P'):
            count += 1

        visited[current_x][current_y] = True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = current_x + dx
            next_y = current_y + dy

            if(next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1):
                continue
            if(board[next_x][next_y] == 'X'):
                continue
            q.append((next_x, next_y))
    return count


visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            result = bfs(i, j)
            if(result == 0):
                print("TT")
            else:
                print(result)
            exit()
