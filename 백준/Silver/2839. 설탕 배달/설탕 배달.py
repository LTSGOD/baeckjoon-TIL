import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

N = int(input())

#경우의수(그리디 하게?)
# 1. 5로만
# 2. 5 + 3
# 3. 3으로만
# 예외
# 반드시 5를 크게 하지 않아도 됨.
# 11 의 경우 5kg 2개사용하면 못담지만 5kg 1개 3kg 2개 하면 가능.

#dp 테이블 생성
#  0 1 2 3  4  5  6  7 8 9 10
#5 X X X X
#3 X X X 1

dp = [[int(1e9) for _ in range(5001)] for _ in range(2)]

dp[1][3] = 1
dp[0][5] = 1

for i in range(3, N+1):
    if dp[0][i] != int(1e9):
        
        if (i + 5 <= N) and (dp[0][i+5] > (dp[0][i] + 1)):
            dp[0][i+5] = (dp[0][i] + 1)
        if (i + 3 <= N) and (dp[1][i+3] > (dp[0][i] + 1)):
            dp[1][i+3] = (dp[0][i] + 1)
    
    if dp[1][i] != int(1e9):
        
        if (i + 5 <= N) and (dp[0][i+5] > (dp[1][i] + 1)):
            dp[0][i+5] = (dp[1][i] + 1)
        if (i + 3 <= N) and (dp[1][i+3] > (dp[1][i] + 1)):
            dp[1][i+3] = (dp[1][i] + 1)

# for row in dp:
#     for i, r in enumerate(row):
#         if i == N+1:
#             break
#         print(r, end= " ")
#     print()

result = min(dp[0][N], dp[1][N])
if result == int(1e9):
    print(-1)
else:
    print(result)