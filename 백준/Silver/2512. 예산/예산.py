import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


N = int(input())

budget = list(map(int, input().split()))

limit = int(input())


# N부터 limit 까지 이진탐색
# 만약 충분히 줄 수 있다면 바로 제일 큰 값 출력
# 아니라면
# T T T T F F F
# 경계에서 start가 최댓값이 되겠지
# 

start = 1
end = max(budget)
mid = 0
def check(mid):
    sum = 0

    #예산들에서 최대금액과 비교 후 더 작은 것을 합한다.
    for b in budget:
        sum += min(b, mid)
    
    #그 합이 총 예산을 넘지 않는다면 True 반환
    if limit >= sum:
        return True
    else:
        return False

#부등호 안붙여서 틀림
if sum(budget) <= limit:
    print(max(budget))
    exit()
else:

    while start + 1 < end:
        mid = (start + end) // 2
        # print(f'start mid end {start, mid, end}')
        if check(mid):
            start = mid
        else:
            end = mid
    print(start)

