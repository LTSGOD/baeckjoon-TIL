import sys
from collections import deque

input = sys.stdin.readline

def dfs(start):

    s = []

    s.append(start)

    while s:
        current = s.pop()

        if visited[current]:
            continue
        visited[current] = True
        print(current, end=" ")

        for n in edge[current]:
            if not visited[n]:
                s.append(n)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        current = q.popleft()

        if visited[current]:
            continue
        visited[current] = True
        print(current, end=" ")

        for n in edge[current]:
            if not visited[n]:
                q.append(n)
N, M, V = map(int, input().split())

edge = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

for i in range(N + 1):
    edge[i].sort(reverse=True)

dfs(V)

visited = [False for _ in range(N + 1)]
for i in range(N + 1):
    edge[i].sort()

print()
bfs(V)



