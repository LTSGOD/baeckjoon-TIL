import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

sudoku = []
coordinate = []

# 실패1: 십자가만 체크하고 영역체크 안함 + 비효율 코드 수정
# 실패2: 좌표값 1개 틀림
# 실패3: 자기자신(0,0)도 체크 해줘야함.


#스도쿠의 채워야 할 좌표를 미리 리스트에 만들어 놓는다.
for i in range(9):
    tmp = list(map(int, input().split()))
    sudoku.append(tmp)

    #0인 좌표 위치 파악
    for j in range(9):
        if tmp[j] == 0:
            coordinate.append((i,j))


#num으로 넘어온 수와 겹치는 것이 있는지 없는지 체크하는 함수
def check(x, y, num):
    #십자가 체크
    for i in range(0, 9):
        if (num == sudoku[i][y]) or (num == sudoku[x][i]):
            return False

    median_x, median_y = 0, 0
    if (x < 3 and y < 3):
        median_x = 1
        median_y = 1
    elif (x < 3 and y < 6):
        median_x = 1
        median_y = 4

    elif (x < 3 and y < 9):
        median_x = 1
        median_y = 7

    elif (x < 6 and y < 3):
        median_x = 4
        median_y = 1
    
    elif (x < 6 and y < 6):
        median_x = 4
        median_y = 4
    
    elif (x < 6 and y < 9):
        median_x = 4
        median_y = 7

    elif (x < 9 and y < 3):
        median_x = 7
        median_y = 1
    
    elif ( x < 9 and y < 6):
        median_x = 7
        median_y = 4

    else:
        median_x = 7
        median_y = 7

    #영역 체크
    for dx, dy in [(0,0),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
        if (num == sudoku[median_x+dx][median_y+dy]):
            return False

    return True

def recursion(depth, index):
    #depth가 빈 0의갯수와 같다면 성공!
    if depth == len(coordinate):

        for line in sudoku:
            for num in line:
                print(num, end=" ")
            print()
        exit()
        
    x = coordinate[index][0]
    y = coordinate[index][1]

    #1 ~ 9 까지 넣어보기
    for num in range(1,10):

        #넣을 수 있다면
        if check(x, y, num):
            #스도쿠에 채우기
            sudoku[x][y] = num
            recursion(depth+1, index+1)
            #스도쿠 다시 비우기
            sudoku[x][y] = 0

recursion(0,0)