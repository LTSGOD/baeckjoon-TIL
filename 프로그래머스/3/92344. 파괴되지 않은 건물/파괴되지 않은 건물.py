def solution(board, skill):
    answer = 0
    
    tmp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d 
        tmp[r1][c1] += d
        tmp[r1][c2 + 1] -= d
        tmp[r2 + 1][c1] -= d
        tmp[r2 +1][c2 + 1] += d
    
    
    for i in range(len(tmp)):
        for j in range(1, len(tmp[0])):
            tmp[i][j] += tmp[i][j - 1]
            
    for j in range(len(tmp[0])):
        for i in range(1, len(tmp)):
            tmp[i][j] += tmp[i - 1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + tmp[i][j] > 0:
                answer += 1
            
    return answer