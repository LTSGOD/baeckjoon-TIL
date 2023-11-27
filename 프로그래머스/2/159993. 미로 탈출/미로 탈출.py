from collections import deque

def bfs(x,y, maps):

    q = deque()
    
    q.append((x,y))
    
    while q:
        current_x, current_y = q.popleft()
        
        for dx, dy in ((1,0),(-1,0), (0,1), (0,-1)):
            next_x = current_x + dx
            next_y = current_y + dy
            
            if next_x < 0 or next_x > H - 1 or next_y < 0 or next_y > W - 1:
                continue
            if maps[next_x][next_y] == "X":
                continue
            if board[current_x][current_y] + 1 < board[next_x][next_y] :
                board[next_x][next_y] = board[current_x][current_y] + 1
                q.append((next_x,next_y))
            
def find_thing(maps, thing):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == thing:
                return i,j

def solution(maps):
    answer = 0
    
    x, y = find_thing(maps, "S")
    l_x, l_y = find_thing(maps, "L")
    e_x,e_y = find_thing(maps, "E")
    global H 
    global W
    global board
    
    H = len(maps)
    W = len(maps[0])
    
    board = [[int(1e9) for _ in range(W)] for _ in range(H)]
    board[x][y] = 0
    
    bfs(x,y,maps)
    
    answer += board[l_x][l_y]
    
    #막다른길 체크
    if answer == int(1e9):
        return -1
    
    board = [[int(1e9) for _ in range(W)] for _ in range(H)]
    board[l_x][l_y] = 0
    bfs(l_x,l_y,maps) 
    
    answer += board[e_x][e_y]
    
    if board[e_x][e_y] == int(1e9):
        return -1 
    
    return answer