import sys
from heapq import heappush, heappop

input = sys.stdin.readline

T = int(input())

#remove 로 삭제하면 시간초과, visited 배열 사용해서 나올 때마다 무시하게 구현.

for _ in range(T):
    k = int(input())

    mean_pq = []
    max_pq = []

    visited = [False] * k
    for i in range(k):
        command = input().rstrip().split()
        num = int(command[1])
        if command[0] == "I":
            heappush(mean_pq, (num,i))
            heappush(max_pq, (-num, i))
        elif command[0] == "D":
            if num == -1:
                while mean_pq and visited[mean_pq[0][1]]:
                    heappop(mean_pq)
                if mean_pq:
                    visited[mean_pq[0][1]] = True
                    heappop(mean_pq)
            else:
                while max_pq and visited[max_pq[0][1]]:
                    heappop(max_pq)
                if max_pq:
                    visited[max_pq[0][1]] = True
                    heappop(max_pq)
    while mean_pq and visited[mean_pq[0][1]]:
                    heappop(mean_pq)
    while max_pq and visited[max_pq[0][1]]:
                    heappop(max_pq)
    if mean_pq and max_pq:
        print(-max_pq[0][0], mean_pq[0][0])
    else:
        print("EMPTY")