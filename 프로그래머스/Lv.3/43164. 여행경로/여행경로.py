def check():
    for key in visited.keys():
        if visited[key] != 0:
            return False
    else:
        return True

def recursion(start):

    if check():
        return True
    
    for dest in 티켓[start]:
        
        if visited[start+dest] == 0:
            continue
        
        visited[start + dest] -= 1
        result.append(dest)
        
        if recursion(dest):
            return True
        
        visited[start + dest] += 1
        result.pop()

def solution(tickets):
    answer = []
    global 티켓
    global visited
    global result

    result = ["ICN"]
    티켓 = dict()
    visited = dict()
    tickets.sort()

    #딕셔너리화
    for t in tickets:
        if t[0] in 티켓:
            티켓[t[0]].append(t[1])
        else:
            티켓[t[0]] = [t[1]]
            
        if t[1] not in 티켓:
            티켓[t[1]] = []
            
    for key in 티켓.keys():
        for v in 티켓[key]:
            if key + v not in visited:
                visited[key + v] = 1
            else:
                visited[key + v] += 1
            
    print(visited)
    recursion("ICN")

    return result