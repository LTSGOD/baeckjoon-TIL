import sys
from collections import deque
input = sys.stdin.readline

total = int(input())


def func(input):
    tmp = []


for _ in range(total):
    N, target = map(int, input().split())

    board = [(i, value)for i, value in enumerate(
        deque(list(map(int, input().split()))))]

    result = 0
    while(board):
        m = max([item[1] for item in board])
        index, value = board[0]
        if(value < m):
            board.append((index, value))
            board.pop(0)
        else:
            board.pop(0)
            result += 1
            if(target == index):
                break
    print(result)
