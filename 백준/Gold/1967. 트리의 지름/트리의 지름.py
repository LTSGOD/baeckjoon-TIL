import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

V = int(input())

#트리에서의 임의의 점에서 가장 먼 노드는 가장 먼거리 노드 양 끝 점 중 하나이다.

edge = [[] for _ in range(V + 1)]
start_node = []

for _ in range(V-1):
    a,b,v = list(map(int, input().split()))
    edge[a].append((b,v))
    edge[b].append((a,v))
    
if V == 1:
    print(0)
    exit()

def bfs(start):
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


#임의의 점 1에서 가장먼 점 선정
visited = [False for _ in range(V+1)]
bfs(1)

answer.sort()
visited = [False for _ in range(V+1)]

#가장 먼점에서 가장 먼거리를 구하면 그것이 최대의 트리의 지름
bfs(answer[-1][1])
answer.sort()
print(answer[-1][0])
