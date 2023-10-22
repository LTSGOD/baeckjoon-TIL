import sys
input = sys.stdin.readline

TC = int(input())

def bellman(start):

    distance[start] = 0
    for s in range(1, N + 1):
        #각 노드 마다 체크
        for i in range(1, N+1):

            # 노드의 모든 간선 체크
            for next_node, value in edge[i]:

                if (distance[i] + value) < distance[next_node]:
                    distance[next_node] = distance[i] + value
                    if s == N:
                        return True
    return False


for _ in range(TC):
    N, M, W = map(int, input().split())

    edge = [[] for _ in range(N + 1)]

    for _ in range(M):
        a,b, v = map(int, input().split())
        edge[a].append((b,v))
        edge[b].append((a,v))

    for _ in range(W):
        a,b, v = map(int, input().split())
        edge[a].append((b,-v))
    
    distance = [int(1e9) for _ in range(N+1)]
    #1번 노드에서 각 경로까지 최단경로
    if bellman(1):
        print("YES")
    else:
        print("NO")