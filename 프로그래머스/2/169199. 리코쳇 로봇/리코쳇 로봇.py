from collections import deque


#좌표 업데이트 시켜주는 함수
def move(s_x, s_y, dx, dy, board):
    
    while True:
        next_x = s_x + dx
        next_y = s_y + dy

        if next_x < 0 or next_x > len(board) - 1 or next_y < 0 or next_y > len(board[0]) - 1 or board[next_x][next_y] == "D":
            return s_x, s_y

        s_x = next_x
        s_y = next_y

        
#bfs 수행
def bfs(x,y,board):
    
    q = deque()
    
    q.append((x,y))
    result[x][y] = 0
    while q:
        current_x, current_y = q.popleft()
        
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            
            next_x, next_y = move(current_x, current_y, dx, dy, board)
            
            if result[current_x][current_y] + 1 < result[next_x][next_y]:
                result[next_x][next_y] = result[current_x][current_y] + 1
                q.append((next_x,next_y))
        

def solution(board):
    
    r_x, r_y = [0,0]
    g_x, g_y = [0,0]
    
    global result
    result = [[int(1e9) for _ in range(len(board[0]))] for _ in range(len(board))]
    
    #좌표 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                r_x = i
                r_y = j
            if board[i][j] == "G":
                g_x = i
                g_y = j
    
    bfs(r_x, r_y,board)
    
    if result[g_x][g_y] == int(1e9):
        return -1
    else:
        return result[g_x][g_y]