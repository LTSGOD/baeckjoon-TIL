import sys
from collections import deque

input = sys.stdin.readline

# 아기 상어가 bfs 탐색(탐색 순서: 위 왼쪽 아래 오른쪽)
# 만약 먹이를 찾았다면 visited 배열 초기화 다시 dfs 시작
# 아니라면 출력(더이상 먹을 게 없다.)

# but 조건을 좀 더 까다롭게 따져야 할 것 같다.
# 위의 방법처럼 하면 그리디 하게 돼서 문제가 원하는 답이 안나옴.
# + 물고기 큰 칸은 못지나간다는 조건 못봄...
N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

eat = 0
distance = 0

def bfs(x, y, size):

    global eat
    global distance

    queue = deque()

    visited = [[False for _ in range(N)] for _ in range(N)]

    queue.append((x,y,0))
    visited[x][y] = True

    #최단 거리 후보 물고기 저장
    candidate = []

    while queue:
        current_x, current_y,current_distance = queue.popleft()

        #현재 방문 노드가 물고기 노드라면
        if board[current_x][current_y] != 0:

            # 몸집 확인 후 후보에 추가
            if board[current_x][current_y] < size:
                candidate.append((current_distance, current_x, current_y))

        # bfs 큐 넣기
        for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            next_x = current_x + dx
            next_y = current_y + dy

            # board의 범위를 넘어가면 
            if next_x < 0 or next_y < 0 or next_x > N - 1 or next_y > N-1:
                continue

            # 자기보다 큰 물고기가 있다면
            if board[next_x][next_y] > size:
                continue
            #아직 방문 하지 않았다면
            if not visited[next_x][next_y]:
                queue.append((next_x, next_y, current_distance+1))
                visited[next_x][next_y] = True

    # 더 이상 후보가 없으면 return
    if not candidate:
        return
    # print(candidate)

    #후보 배열 정렬 오름 차순이기 때문에 거리, x, y가 문제 조건 대로 정렬됨.
    candidate.sort()

    #냠냠
    eat += 1

    #만약 먹은 물고기 수가 몸집만큼 된다면
    if eat == size:

        # 몸집 크기 키우고 먹은 물고기 수 추기화
        size += 1
        eat = 0

    #최소 거리 갱신
    distance += candidate[0][0]

    #먹은 물고기 위치 초기화
    board[candidate[0][1]][candidate[0][2]] = 0

    # for i in board:
    #     print(i)
    # print(f'eat {eat} size {size} distance {distance}')
    # print("-------------------------")

    #해당 위치부터 다시 bfs 시작
    bfs(candidate[0][1], candidate[0][2], size)

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            bfs(i, j, 2)

print(distance)