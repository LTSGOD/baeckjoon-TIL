import sys
from heapq import heappush, heappop
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
s = int(input())
INF = int(1e9)

distance = [INF] * (V+1)
edges = [[] for i in range(V + 1)]

def djkstra(start):
    hq = []
    heappush(hq, (0, start))

    distance[start] = 0

    while hq:
        dist, current = heappop(hq)

        if distance[current] < dist:
            continue
        
        for i in edges[current]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))





for _ in range(E):
    u,v,w = map(int, input().split())
    edges[u].append((v,w))

djkstra(s)

for index, i in enumerate(distance):
    if index == 0:
        continue
    if i == INF:
        print("INF")
    else:
        print(i)

