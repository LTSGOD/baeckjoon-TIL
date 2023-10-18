import sys

import heapq

input = sys.stdin.readline

N = int(input())

schedule = []

# 앞에 DP 에 해당하는 자료구조를 set까지로 바꿨는데
# set이 아닌 heap을 사용하면 시간을 줄일 수 있었다.
# heapq 삽입, 삭제 시 정렬시간 log n이므로
# 전체 nlogn 시간에 끝낼 수 있음.

for _ in range(N):
    a, b= map(int, input().split())
    schedule.append((a,b))

schedule.sort()

room = []
heapq.heappush(room,schedule[0][1])
count = 1
for i, (s, e) in enumerate(schedule):
    if i == 0:
        continue
    if room[0] <= s:
        heapq.heappop(room)
        heapq.heappush(room, e)
    else:
        heapq.heappush(room, e)
        count += 1

print(count)