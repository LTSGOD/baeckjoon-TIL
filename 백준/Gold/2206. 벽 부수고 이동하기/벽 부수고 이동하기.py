import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

#bfs로 가는데 벽부술수있는 상태와 아닌 상태로 최단거리 찾기

N, M = map(int, input().split())

board = [[],[]]

#3차원 배열 설정
# 1층에서 벽을 만나면 2층으로 보내서 최단거리를 찾는다.
for _ in range(N):
    tmp = list(map(int, input().rstrip()))
    tmp2 = [*tmp]
    board[0].append(tmp)
    board[1].append(tmp2)


def bfs(x, y):

    q = deque()

    # x, y, floor
    q.append((x,y,0))

    while q:
        current_x, current_y, current_floor = q.popleft()

        for dx, dy in ([0,1], [1,0],[0,-1],[-1,0]):
            next_x = current_x + dx
            next_y = current_y + dy

            if next_x < 0 or next_y < 0 or next_x > N -1 or next_y > M - 1:
                continue
            

            #다음 길이 0일 때 방문하지 않았다면 정상 bfs
            if (board[current_floor][next_x][next_y] == 0):
                board[current_floor][next_x][next_y] = board[current_floor][current_x][current_y] + 1
                q.append((next_x,next_y, current_floor))
            #다음 길이 벽인데 0층 이고 아직 방문하지 않았다면
            elif (current_floor == 0) and (board[current_floor][next_x][next_y] == 1):
                board[1][next_x][next_y] = board[0][current_x][current_y] + 1
                q.append((next_x, next_y, 1))

board[0][0][0] = 1
board[1][0][0] = 1

bfs(0,0)

if (board[0][N-1][M-1] == 0) and (board[1][N-1][M-1] == 0):
    print(-1)
elif board[0][N-1][M-1] == 0:
    print(board[1][N-1][M-1])
elif board[1][N-1][M-1] == 0:
    print(board[0][N-1][M-1])
else:
    print(min(board[0][N-1][M-1],board[1][N-1][M-1]))