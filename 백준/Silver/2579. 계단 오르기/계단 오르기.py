import sys

input = sys.stdin.readline

N = int(input())

계단 = [0]

for _ in range(N):
    계단.append(int(input()))

dp = [0 for _ in range(N+1)]

if N == 1:
    print(계단[1])
    exit()
elif N == 2:
    print(sum(계단))
else:
    dp[1] = 계단[1]
    dp[2] = 계단[1] + 계단[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + 계단[i-1], dp[i-2]) + 계단[i]

    print(dp[-1])