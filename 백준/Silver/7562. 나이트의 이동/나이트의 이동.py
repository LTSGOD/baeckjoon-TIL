import sys
from collections import deque

input = sys.stdin.readline

# 최소 몇번만에 이동하는지 출력하는 것이기 때문에 bfs사용
# board에다가 거리 기록

def bfs(x,y):
    queue = deque()

    queue.append((x,y))
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()

        # 갈 수 있는 방향에 대해 탐색
        for dx, dy in [(-2,1),(-2,-1),(1,2),(-1,2),(2,1),(2,-1),(1,-2),(-1,-2)]:
            next_x = current_x + dx
            next_y = current_y + dy

            if next_x < 0 or next_y < 0 or next_x > I - 1 or next_y  > I - 1:
                continue
            if visited[next_x][next_y] == False:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

                #거리 기록
                board[next_x][next_y] = board[current_x][current_y] + 1
T = int(input())

for _ in range(T):
    I = int(input())

    s_x, s_y = map(int, input().split())

    e_x, e_y = map(int, input().split())

    board = [[0 for _  in range(I)] for _ in range(I)]
    visited = [[False for _ in range(I)] for _ in range(I)]

    bfs(s_x, s_y)

    # for i in board:
    #     print(i)

    print(board[e_x][e_y])
