import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y):
    count = 0

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if(next_x < 0 or next_x > R - 1 or next_y < 0 or next_y > C-1):
            continue
        if(board[next_x][next_y] == '.'):
            count += 1
    return count


flag = True
for i in range(R):
    for j in range(C):
        if(board[i][j] == 'X'):
            continue
        if(check(i, j) == 1):
            print(1)
            exit()
print(0)