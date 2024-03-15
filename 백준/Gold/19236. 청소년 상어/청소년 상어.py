import sys
from copy import deepcopy

input = sys.stdin.readline

answer = -1
fish_map = {}
board = []

먹은물고기 = 0
shark_x = 0
shark_y = 0
shark_dir = 0

direction = [(-1,0),(-1,-1), (0,-1), (1, -1), (1,0),(1,1),(0,1),(-1,1)]

def fish_move(board, fish_map, shark_x, shark_y):

  for i in range(1, 17):

    if fish_map.get(i):
      current_x = fish_map[i][0]
      current_y = fish_map[i][1]
      dir_num = fish_map[i][2] - 1

      #방향 체크
      for _ in range(8):
        dx = direction[dir_num % 8][0]
        dy = direction[dir_num % 8][1]

        next_x = current_x + dx
        next_y = current_y + dy

        #판밖으로 나갈경우
        if next_x < 0 or next_y < 0 or next_x > 3 or next_y > 3:
          dir_num += 1
          continue
        #상어가 있을 경우
        if (next_x == shark_x) and (next_y == shark_y):
          dir_num += 1
          continue
        # if i == 6:
        #   print(current_x, current_y, dir_num)
        #   print(next_x, next_y)
        #방향업데이트
        board[current_x][current_y][1] = (dir_num % 8) + 1 #방향 업데이트

        #물고기 위치 맵 업데이트
        fish_map[i] = (next_x, next_y, dir_num + 1)
        # print(current_x, current_y)
        # print(next_x, next_y)

        #바꿀자리에 물고기가 있으면
        if board[next_x][next_y] != []:
          n = board[next_x][next_y][0]
          dir = board[next_x][next_y][1]
          fish_map[n] = (current_x, current_y, dir)

        #물고기 교환
        tmp = board[next_x][next_y]
        board[next_x][next_y] = board[current_x][current_y]
        board[current_x][current_y] = tmp
        break
    else:
      continue
    # if i == 2:
    #   break

for i in range(4):
  tmp = list(map(int, input().split()))
  j =0
  a = []
  while j < 4:
    if i == 0 and  j == 0:
      먹은물고기 = tmp[j]
      shark_dir = tmp[j+1]

    else:
      fish_map[tmp[j * 2]] = (i,j,tmp[j*2+1])
    a.append([tmp[j*2],tmp[j*2+1]])
    j += 1
  board.append(a)
  
board[0][0] = []

stack = []

#상어x, 상어y,먹은물고기 수, 상어방향, board, fish_map
stack.append((0,0,먹은물고기,shark_dir, board, fish_map))

while stack:

  current_x, current_y, 먹은물고기, shark_dir, board, fish_map = stack.pop()
  #생선이동
  # print(current_x, current_y)
  # print("shark 방향: ", shark_dir)
  # print("먹은물고기: ", 먹은물고기)
  # for row in board:
  #   print(row)

  fish_move(board, fish_map, current_x, current_y)

  # print()
  # for row in board:
  #   print(row)

  dx = direction[shark_dir - 1][0]
  dy = direction[shark_dir - 1][1]

  #최대 3번 이동가능
  for i in range(1,4):

    next_x = current_x + (dx * i)
    next_y = current_y + (dy * i)

    #범위 넘으면 멈추기
    if next_x < 0 or next_y < 0 or next_x > 3 or next_y > 3:
      
      #범위 넘었으면 더이상 갈때 없는것.
      if answer < 먹은물고기:
        answer = 먹은물고기
      break

    #물고기 없는칸이면
    if board[next_x][next_y] == []:
      continue
    else:

      #deepcopy
      board_c = deepcopy(board)
      fish_map_c = deepcopy(fish_map)

      fish_num = board[next_x][next_y][0]

      #물고기냠냠
      fish_map_c.pop(fish_num)
      board_c[next_x][next_y] = []

      stack.append((next_x, next_y, 먹은물고기 + fish_num,board[next_x][next_y][1], board_c, fish_map_c))






# print(board)
# fish_move(board)
# print(fish_map)
# for row in board:
#   print(row)

print(answer)

