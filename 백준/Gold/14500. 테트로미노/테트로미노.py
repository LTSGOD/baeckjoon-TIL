import sys
from math import sqrt

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = []

def check1(x,y):

    #가로
    if y + 3 < M:
        tmp = 0
        for i in range(4):
            tmp += board[x][y+i]
        result.append(tmp)

    #세로
    if x + 3 < N:
        tmp = 0
        for i in range(4):
            tmp += board[x+i][y]
        result.append(tmp)

def check2(x,y):
    if x + 1 < N and y +1 < M:
        tmp = board[x][y] + board[x][y+1] + board[x+1][y] + board[x + 1][y +1]
        result.append(tmp)

def check3(x,y):
    if y + 1 < M and x + 2 < N:
        tmp = board[x][y] + board[x + 1][y] + board[x +2][y] + board[x+2][y+1]
        result.append(tmp)
        tmp = board[x][y] + board[x + 1][y] + board[x +2][y] + board[x][y+1]
        result.append(tmp)
 
    if y - 1 >= 0 and x + 2 < N:
        tmp = board[x][y] + board[x + 1][y] + board[x +2][y] + board[x+2][y-1]
        result.append(tmp)
        tmp = board[x][y] + board[x + 1][y] + board[x +2][y] + board[x][y-1]
        result.append(tmp)
    if y + 2 < M and x + 1 < N:
        tmp = board[x][y] + board[x][y+1] + board[x][y+2] + board[x+1][y]
        result.append(tmp)
        tmp = board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+1][y+2]
        result.append(tmp)
    if y -2 >= 0 and x + 1 < N:
        tmp = board[x][y] + board[x+1][y] + board[x][y-1] + board[x][y-2]
        result.append(tmp)
        tmp = board[x][y] + board[x+1][y] + board[x+1][y-1] + board[x+1][y-2]
        result.append(tmp)

def check4(x,y):
    if x + 2 < N and y + 1 < M:
        tmp = board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+2][y+1]
        result.append(tmp)
    if x + 1 < N and y -1 >= 0 and y + 1 < M:
        tmp = board[x][y] + board[x+1][y] + board[x][y+1] + board[x+1][y-1]
        result.append(tmp)
        tmp = board[x][y] + board[x+1][y] + board[x][y-1] + board[x+1][y+1]
        result.append(tmp)
    if x - 1 >= 0 and x + 1 < N and y + 1 < M:
        tmp = board[x][y] + board[x][y+1] + board[x-1][y+1] + board[x+1][y] 
        result.append(tmp)

def check5(x,y):
    if y + 2 < M and x + 1 < N:
        tmp = board[x][y] + board[x][y+1] + board[x][y+2] + board[x+1][y+1]
        result.append(tmp)
    if y + 2 < M and x -1 >= 0:
        tmp = board[x][y] + board[x][y+1] + board[x][y+2] + board[x-1][y+1]
        result.append(tmp)
    if x +2 < N and y + 1 <M:
        tmp = board[x][y] + board[x+1][y] + board[x+2][y] + board[x+1][y+1]
        result.append(tmp)
    if x + 2 < N and y - 1 >= 0:
        tmp = board[x][y] + board[x+1][y] + board[x+2][y] + board[x+1][y-1]
        result.append(tmp)
for i in range(N):
    for j in range(M):
        check1(i,j)
        check2(i,j)
        check3(i,j)
        check4(i,j)
        check5(i,j)

result.sort(reverse=True)
print(result[0])
# 20000000 최대 이정도? 