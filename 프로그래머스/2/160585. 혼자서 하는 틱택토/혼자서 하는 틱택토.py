

def isOver(board):
    오성공 = 0
    엑스성공 = 0 
    #가로줄 체크
    for i in range(3):
        기준 = board[i][0]
        if 기준 ==".":
            continue
        for j in range(1,3):
            
            #한줄이 똑같지않으면 게임 안끝남
            if 기준 != board[i][j]:
                break
        #무사히끝났다면 게임 종료
        else:
            if 기준 == "X":
                엑스성공 += 1
            else:
                오성공 += 1 
    #세로줄 체크
    for i in range(3):
        기준 = board[0][i]
        if 기준 ==".":
            continue
        for j in range(1,3):
            
            #한줄이 똑같지않으면 게임 안끝남
            if 기준 != board[j][i]:
                break
        #무사히끝났다면 게임 종료
        else:
            if 기준 == "X":
                엑스성공 += 1
            else:
                오성공 += 1
    
    #우하향 대각선 체크
    기준 = board[0][0]
    if 기준 !=".":
        for i in range(1,3):
            if 기준 != board[i][i]:
                break
        else:
            if 기준 == "X":
                엑스성공 += 1
            else:
                오성공 += 1
    
    #우상향 대각선 체크
    기준 = board[0][2]
    if 기준 !=".":
        for i in range(1,3):
            if 기준 != board[i][2-i]:
                break
        else:
            if 기준 == "X":
                엑스성공 += 1
            else:
                오성공 += 1
        
    return 오성공, 엑스성공
def solution(board):
    o_coordinate = []
    x_coordinate = []
    
    answer = -1
    
    for i, line in enumerate(board):
        for j, tmp in enumerate(line):
            if tmp == "O":
                o_coordinate.append((i,j))
            elif tmp =="X":
                x_coordinate.append((i,j))
    
    o_num = len(o_coordinate)
    x_num = len(x_coordinate)
    오성공, 엑스성공 = isOver(board)
    
    if o_num > x_num:
        
        if o_num == (x_num + 1):
            
            # o_num 이 4보다작은경우는 다 가능
            if o_num < 4:
                return 1
            else:
                if 엑스성공 > 0:
                    return 0
                else:
                    return 1
                    
        else:
            return 0
    elif x_num > o_num:
        return 0
    else:
        if 오성공 > 0:
            return 0
        else:
            return 1

    