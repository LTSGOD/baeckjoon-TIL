import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
inf = 100000

edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


def BFS(start):
    q = deque()
    q.append(start)
    board[start] = 0
    board[0] = 0

    while(q):
        current = q.popleft()

        if(visited[current] == True):
            continue
        visited[current] = True

        for next in edge[current]:
            if(board[next] > board[current] + 1):
                board[next] = board[current] + 1
            q.append(next)


result = []
for i in range(1, N+1):
    visited = [False] * (N + 1)
    board = [inf] * (N + 1)
    BFS(i)
    result.append(sum(board))

print(result.index(min(result)) + 1)
