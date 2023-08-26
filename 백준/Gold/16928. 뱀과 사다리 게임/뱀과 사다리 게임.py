import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

teleport = []
INF = int(1e9)
board = [INF] * 101 

for _ in range(N+M):
    a,b = map(int, input().split())
    teleport.append([a,b])


def bfs(start):
    q = deque()
    q.append((start,0))

    while q:
        current, cnt = q.popleft()

        if board[current] < cnt:
            continue
        
        cnt+=1

        for dice in range(1,7):
            next = current + dice


            for start, end in teleport:
                if next == start:
                    next = end

            if next > 100:
                continue
            if cnt < board[next]:
                board[next] = cnt
                q.append((next, cnt)) 

bfs(1)

print(board[100])