import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

짝꿍표 = {}
배치 = [[0 for _ in range(N)] for _ in range(N)]
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
순서 = []
answer = 0

for _ in range(N ** 2):
  name, f1, f2, f3, f4 = list(map(int, input().split()))

  짝꿍표[name] = {f1:1,  f2:1, f3:1, f4:1}
  순서.append(name)

#첫 친구부터
for name in 순서:

  칸후보 = []

  #각 칸에 대하여
  for i in range(N):
    for j in range(N):
      
      #이미 친구가 있으면 pass
      if 배치[i][j] != 0:
        continue

      cond1 = 0
      cond2 = 0
    
      #주변탐색
      for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
        next_x = i + dx
        next_y = j + dy

        #범위밖이면
        if next_x < 0 or next_y < 0 or next_x > N - 1 or next_y > N - 1:
          continue
        
        #빈칸이면
        if 배치[next_x][next_y] == 0:
          cond2 += 1
        #친구있으면
        else:
          if 짝꿍표[name].get(배치[next_x][next_y]):
            cond1 += 1
      
      #칸후보 저장
      칸후보.append((cond1, cond2, i, j))

  칸후보.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2], -x[3]))

  x = 칸후보[0][2]
  y = 칸후보[0][3]
  배치[x][y] = name

  # for line in 배치:
  #   print(line)
  # print()


for i in range(N):
  for j in range(N):
    name = 배치[i][j]
    count = 0

    for dx, dy in [(0,1), (1,0), (0, -1), (-1, 0)]:
      next_x = i + dx
      next_y = j + dy

      if next_x <0 or next_y <0 or next_x > N-1 or next_y > N-1:
        continue

      if 짝꿍표[name].get(배치[next_x][next_y]):
        count += 1
    answer += score[count]
  
print(answer)
