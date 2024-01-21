from collections import deque

def bfs(visited, start):
    
    q = deque()
    
    q.append(start)
    visited[start] = 0
    
    while q:
        current = q.popleft()
        
        for next_node in roads_list[current]:
            
            if visited[current] + 1 < visited[next_node]:
                visited[next_node] = visited[current] + 1
                q.append(next_node)
                


def solution(n, roads, sources, destination):
    answer = []
    global roads_list
    roads_list = [[] for _ in range(n + 1)]
    
    for s, e in roads:
        roads_list[s].append(e)
        roads_list[e].append(s)
    
    visited = [int(1e9) for _ in range(n + 1)]
        
    bfs(visited, destination)
    for s in sources:
        if visited[s] == int(1e9):
            answer.append(-1)
        else:
            answer.append(visited[s])
        # print(visited)
    

    return answer