def dfs(n, computers):
    global visited    

    s = []
    
    if visited[n]:
        return False
    s.append(n)
    visited[n] = True
    
    while s:
        current = s.pop()
        
        for index, 연결여부 in enumerate(computers[current]):
            if (연결여부 == 1) and not visited[index]:
                s.append(index)
                visited[index] = True
    
    return True

def solution(n, computers):
    global visited
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if dfs(i, computers):
            answer += 1

    return answer