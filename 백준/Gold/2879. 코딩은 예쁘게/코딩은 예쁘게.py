import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

C = [B[i] - A[i] for i in range(N)]

i = 1
result = abs(C[0])
max = 0
while i < len(C):
    #부호가 다르면
    if C[i-1] * C[i] < 0:
        result += abs(C[i])
    
    #부호가 같다면
    else:
        #이전 것보다 뒤에 있는 것이 크다면
        if abs(C[i-1]) < abs(C[i]):
            result += (abs(C[i]) - abs(C[i-1]))

        #이전 것보다 뒤에 있는 것이 작다면 같이삭제해주면 되므로 처리 할 필요 X
    i+=1

# print(C)
print(result)
#4 2 0 2 4
#처음 한 생각
#B - A를 해준다음 부호가 달라 질 때를 한뭉탱이로 계산
# but 반례 생성. 부호가 같아도 중간중간 0 이 껴있으면 틀린답

#다음 생각
#각 구간에서 최솟값을 구한 후 더해 준 후 모든 배열이 0이 될때까지 반복
# 시간초과 이슈...

# 모르겠어서 답을 봣는데 굉장히 쉬운 그리디였다.
# 그냥 한개씩 보며