from collections import deque

def bfs(start):
    
    q = deque()
    
    q.append(start)
    distance[start] = 0
    
    
    while q:
        current_node = q.popleft()
        
        for next_node in edge_info[current_node]:
            
            if distance[current_node] + 1 < distance[next_node]:
                distance[next_node] = distance[current_node] + 1
                q.append(next_node)
            
    
    pass
def solution(n, edge):
    answer = 0
    
    global edge_info
    global distance
    edge_info = [[] for _ in range(n+1)]
    distance = [int(1e9) for _ in range(n+1)]
    distance[0] = -int(1e9)
    
    for s,e in edge:
        edge_info[s].append(e)
        edge_info[e].append(s)
    
    bfs(1)
    # print(distance)
    return distance.count(max(distance))