import heapq
    
def solution(n, paths, gates, summits):
    INF = int(1e9)
    
    new_path = [[] for i in range(n+1)]
    
    for i,j,w in paths:
        new_path[i].append((j,w))
        new_path[j].append((i,w))

    def djkstra():
        hq = []
        
        for gate in gates:
            heapq.heappush(hq, (0, gate))
            intensity[gate] = 0

        while hq:
            intense, current = heapq.heappop(hq)

            if intense > intensity[current]:
                continue
            if current in summits:
                continue
                
            for j,w in new_path[current]:
                #다른문이면

                tmp = w if intensity[current] < w else intensity[current]
                
                if tmp < intensity[j]:
                    intensity[j] = tmp
                    heapq.heappush(hq, (tmp, j))

    result = []
    intensity = [INF] * (n+1)

    djkstra()
    for summit in summits:
        result.append((intensity[summit], summit))
    result = min(result)
    answer = [result[1], result[0]]
    return answer