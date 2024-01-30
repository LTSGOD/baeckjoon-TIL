
#max_dp는 i j 까지 최댓값
#min_dp는 i, j에서 최솟값


def solution(arr):
    answer = -1
        
    
    num = len(arr) // 2 + 1

    max_dp = [[-int(1e9) for _ in range(num)] for _ in range(num)]
    
    min_dp = [[int(1e9) for _ in range(num)] for _ in range(num)]
    
    for step in range(num):
        
        for i in range(num-step):
            j = i + step
            if i == j :
                max_dp[i][j] = int(arr[i * 2])
                min_dp[i][j] = int(arr[i * 2])
            # elif j == i + 1:
            #     if arr[i * 2 + 1] == "+":  
            #         max_dp[i][j] = int(arr[i*2]) + int(arr[i*2 + 2])
            #         min_dp[i][j] = int(arr[i*2]) + int(arr[i*2 + 2])
            #     else:
            #         max_dp[i][j] = int(arr[i*2]) - int(arr[i*2 + 2])
            #         min_dp[i][j] = int(arr[i*2]) - int(arr[i*2 + 2])
            else:
                for k in range(i, j):
                    # print(arr[k*2+1])
                    if arr[k * 2 + 1 ] == "+":
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                    else:
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    # print(max_dp)
    # print(min_dp)
    return max_dp[0][-1]