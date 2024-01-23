def solution(m, n, puddles):

    board = [[0 for _ in range(m+1)] for _ in range(n+1)] 
    
    연못위치= [[False for _ in range(m+1)] for _ in range(n+1)]
    
    for y, x in puddles:
        연못위치[x][y] = True
        
    board[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+ 1):
            if i == 1 and j == 1:
                continue
            if 연못위치[i][j]:
                continue
            board[i][j] = board[i-1][j] % 1000000007 + board[i][j-1] % 1000000007
    
    
    return board[n][m] % 1000000007