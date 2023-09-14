import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

edge = [[] for i in range(N + 1)]

for _ in range(N - 1):
    a,b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

visited = [False]* (N+1)

result = [[] for i in range(N+1)]


def dfs(num):

    s = deque()

    s.append(num)

    while s:
        current = s.pop()

        visited[current] = True

        for i in edge[current]:
            if visited[i] == True:
                continue
            s.append(i)
            result[i].append(current)

dfs(1)

for i in range(2,N+1):
    print(result[i][0])

# 재귀 함수 사용시 recursion error
# def recursion(num, node):
#     visited[num] = True

#     for n in node:
#         if visited[n]:
#             continue
#         result[n].append(num)
#         recursion(n,edge[n])

#     return