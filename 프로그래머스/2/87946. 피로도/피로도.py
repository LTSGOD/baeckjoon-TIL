
def recursion(depth, dungeons, k):
    global answer
    
    if depth == len(dungeons):
        
        체력 = k
        count = 0
        for i in result:
            mini = dungeons[i][0]
            cost = dungeons[i][1]
            if 체력 >= mini:
                체력 -= cost
                count += 1
        if count > answer:
            answer = count
        return
    
    for i in index:
        
        if visited[i]:
            continue
            
        result.append(i)
        visited[i] = True
        recursion(depth + 1, dungeons, k)
        visited[i] = False
        result.pop()
        

def solution(k, dungeons):
    global index
    global visited
    global result
    global answer
    index = [i for i in range(len(dungeons))]
    visited = [False for i in range(len(dungeons))]
    result = []
    
    answer = -1
    
    
    recursion(0, dungeons, k)
    
    return answer