import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

V = int(input())

edge = [[] for _ in range(V + 1)]
start_node = []

for _ in range(V):
    tmp = list(map(int, input().split()))
    index = tmp[0]
    for i in range(1,len(tmp),2):
        if tmp[i] == -1:
            continue
        edge[index].append((tmp[i], tmp[i + 1]))

  

def dfs(start):
    queue = deque()

    queue.append((start,0))

    while queue:
        current, result = queue.popleft()

        visited[current] = True

        for next, next_value in edge[current]:
            if visited[next] == True:
                continue
            queue.append((next, result+next_value))
            answer.append((result+next_value, next))

answer = []

visited = [False for _ in range(V+1)]
dfs(1)

answer.sort()
visited = [False for _ in range(V+1)]

dfs(answer[-1][1])
answer.sort()
print(answer[-1][0])
