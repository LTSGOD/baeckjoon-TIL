import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    start = (0, 0)
    q = deque()
    q.append(start)

    while q:
        cx, cy = q.popleft()
        for dx, dy in delta:
            nx = cx + dx
            ny = cy + dy
            if(nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1):
                continue

            if(graph[nx][ny] == 0):
                continue
            if(graph[nx][ny] == 1):
                graph[nx][ny] = graph[cx][cy] + 1
                q.append((nx, ny))


n, m = map(int, input().split())

graph = [list(map(int, input().rstrip()))for _ in range(n)]
delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]

BFS()
print(graph[n-1][m-1])
