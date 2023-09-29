import sys

input = sys.stdin.readline

N = int(input())

# 두 건물의 높이를 더하고 나누기 2로 처리
# 근데 위치정보도 고려되니까 기울기로 풀어야겟다.

height = list(map(int, input().split()))

i = 0
max_v = 0
while i < N:
    dp = [[] for _ in range(N)]
    dp[i] = -int(1e9)
    count = 0
    #오른쪽 건물 체크
    for j in range(i+1,N):
        slope = (height[j] - height[i]) / (j - i)
        # print(slope, dp[j-1])
        #전 건물의 기울기보다 더 크다면 
        if slope > dp[j-1]:
            count += 1

        dp[j] = max(slope, dp[j-1])
    
    # print(count, end=" ")
    dp[i] = int(1e9)
    #왼쪽 건물 체크
    for j in range(i-1, -1, -1):
        slope = (height[i] - height[j]) / (i-j)

        #전 건물의 기울기보다 더 크다면 
        if slope < dp[j+1]:
            count +=1
        dp[j] = min(slope,dp[j+1])
    i+=1
    if count > max_v:
        max_v = count
    # print(count)
    # print("------------------------------")
print(max_v)