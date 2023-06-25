import sys
from collections import deque
input = sys.stdin.readline


def DFS(v):

    stack = deque()
    stack.append(v)

    while(stack):
        current = stack.pop()

        if(visited[current] == True):
            continue

        dfs_list.append(current)
        visited[current] = True

        for node in sorted(edge[current], reverse=True):
            stack.append(node)


def BFS(v):

    q = deque()
    q.append(v)

    while(q):
        current = q.popleft()
        if(visited[current] == True):
            continue

        bfs_list.append(current)
        visited[current] = True
        for node in sorted(edge[current]):
            q.append(node)


n, m, v = map(int, input().split())

edge = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

dfs_list = []
bfs_list = []
DFS(v)
visited = [False] * (n + 1)
BFS(v)

print(*dfs_list)
print(*bfs_list)
