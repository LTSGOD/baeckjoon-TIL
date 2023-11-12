import sys

input = sys.stdin.readline

A = input().rstrip()

B = input().rstrip()

dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A) +1):

        #문자가 같다면 +1
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for row in dp:
#     print(row)

print(dp[len(B)][len(A)])