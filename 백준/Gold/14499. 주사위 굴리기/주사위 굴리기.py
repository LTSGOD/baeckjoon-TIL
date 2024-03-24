import sys

input = sys.stdin.readline

def 주사위굴리기(board, dir):
  global x
  global y
  global 세로면
  global 가로면
  global 위

  방향 = [(), (0,1),(0,-1),(-1,0), (1, 0)]

  next_x = x + 방향[dir][0]
  next_y = y + 방향[dir][1]

  #방향 벗어나면
  if next_x < 0 or next_y < 0 or next_x > N -1 or next_y > M -1:
    return

  if dir == 1:

    #주사위 굴리기
    tmp = 가로면[0]

    가로면 = 가로면[1:] + [위]
    위 = tmp

    세로면[1] = 가로면[1]

    #주사위 복사

    가로면[1] = 세로면[1] = 주사위복사(board, next_x, next_y, 가로면[1])

  elif dir == 2:
    #굴리기
    tmp = 가로면[2]

    가로면 = [위] + 가로면[:2]
    위 = tmp
    세로면[1] = 가로면[1]

    #복사
    가로면[1] = 세로면[1] = 주사위복사(board, next_x, next_y, 가로면[1])
  elif dir == 3:
    #굴리기
    tmp = 세로면[2]

    세로면 = [위] + 세로면[:2]
    위 = tmp
    가로면[1] = 세로면[1]

    가로면[1] = 세로면[1] = 주사위복사(board, next_x, next_y, 가로면[1])
  else:
    #주사위 굴리기
    tmp = 세로면[0]
    # print("12", 세로면)
    세로면 = 세로면[1:] + [위]
    위 = tmp
    # print("13", 세로면)

    가로면[1] = 세로면[1]

    #주사위 복사

    가로면[1] = 세로면[1] = 주사위복사(board, next_x, next_y, 가로면[1])
  
  print(위)
  x = next_x
  y = next_y

def 주사위복사(board, next_x, next_y, 바닥면):
  if board[next_x][next_y] == 0:
    board[next_x][next_y] = 바닥면
  else:
    바닥면 = board[next_x][next_y]
    board[next_x][next_y] = 0
  return 바닥면

global x
global y

N, M ,x, y, K = list(map(int, input().split()))

board = []

for _ in range(N):
  board.append(list(map(int, input().split())))

instruction = list(map(int, input().split()))

global 세로면
global 가로면
global 위

세로면 = [0,0,0]
가로면 = [0,0,0]
위 = 0

for i in instruction:
  주사위굴리기(board,  i)