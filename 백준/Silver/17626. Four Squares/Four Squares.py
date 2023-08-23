import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())
INF = int(1e9)
dp = [INF] * (50001)

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(1,int(sqrt(n))+1):
    dp[i*i] = 1

for i in range(4, n + 1):

    if dp[i] != INF:
        continue
    j = 1
    while j*j <= i:
        if dp[i] == INF:
            dp[i] = dp[j*j] + dp[i-j*j]
        else:
            dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])
        j+=1
print(dp[n])