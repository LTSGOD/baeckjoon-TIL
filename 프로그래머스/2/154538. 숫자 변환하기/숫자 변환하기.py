from collections import deque

def bfs(start, y,n):
    
    q = deque()
    
    q.append(start)
    result[start] = 0
    
    while q:
        current = q.popleft()
        for i, v in enumerate([n, 2, 3]):
            다음 = 0
            
            #다음 수 세팅
            if i == 0:
                다음 = current + n
            elif i == 1:
                다음 = current * 2
            else:
                다음 = current * 3
            
            #타겟 범위를 넘어갈 경우
            if 다음 > y:
                continue
            
            #만약 다음 최소연산횟수보다 더 작다면
            if result[다음] > result[current] + 1:
                result[다음] = result[current] + 1
                q.append(다음)

def solution(x, y, n):
    answer = 0
    global result
    result = [int(1e9) for _ in range(y+1)]
    bfs(x,y,n)
    
    if result[y] == int(1e9):
        return -1
    else:
        return result[y]
    return answer