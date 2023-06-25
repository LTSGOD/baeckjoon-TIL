import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

a, b = map(int, input().split())


def BFS(start):
    visited = [False] * n
    q = deque()
    q.append(start)

    while(q):
        current = q.popleft()

        if(visited[current] == True):
            continue
        visited[current] = True
        for node in edge[current]:
            q.append(node)
            if(board[node] == 0 or board[node] > board[current] + 1):
                board[node] = board[current] + 1
        # print(f'current node: {current} board: {board}')


edge = []
for i, num in enumerate(l):
    tmp = [j for j in range(i, n, num) if(j != i)]
    for j in range(i, -1, -num):
        if(j == i):
            continue
        tmp.append(j)
    edge.append(tmp)

board = [0] * n
# print(edge)
BFS(a-1)
# print(board)
if(board[b-1] == 0):
    print(-1)
else:
    print(board[b-1])
