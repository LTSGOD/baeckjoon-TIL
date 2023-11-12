import sys

input = sys.stdin.readline

N, K = map(int, input().split())

물건 = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N+1)]

for _ in range(N):
    물건.append([*map(int, input().split())])

for i in range(1, N+1):
    for 배낭크기 in range(1, K + 1):
        
        #물건 배낭에 넣을 수 있다면
        if 배낭크기 >= 물건[i][0]:

            #현재최대가치 = max(이전줄최대가치, 넣을물건가치 + 물건넣고남는공간의최대가치)
            dp[i][배낭크기] = max(dp[i-1][배낭크기], (물건[i][1] + dp[i-1][배낭크기- 물건[i][0]]))
        else:
            #현재최대가치 = 이전줄최대가치
            dp[i][배낭크기] = dp[i-1][배낭크기]

print(dp[N][K])