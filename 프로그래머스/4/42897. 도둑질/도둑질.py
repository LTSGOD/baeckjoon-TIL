#힙을 이용해서
# 1개 털떼 최대
# 1 2 3 4 5 6 7

# 2개 털때 최대

# 7 9 10 11 12 10 12

# 3개 털때 최대

# dp 의 값 0번째 집부터 현재집까지 훔칠 수 있는 최댓값
# 2가지 경우의 수 dp 사용
# dp1 -> 1 번째 집 털고 2번째 집
# dp2 -> 2번째집부터 털기
def solution(money):
    answer = 0
    
    dp1 = [i for i in money]
    dp2 = [i for i in money]

    dp1[1] = -1
    dp1[2] = dp1[0] + dp1[2]
    
    dp2[0] = -1
    
    for i in range(3,len(money)):
        dp1[i] += max(dp1[i - 2],  dp1[i - 3])
        dp2[i] += max(dp2[i - 2], dp2[i - 3])
    
    # print(dp1)
    # print(dp2)
    dp1_max  = max(dp1[len(money) - 2], dp1[len(money)- 3])
    dp2_max = max(dp2[len(money) - 1],  dp2[len(money) - 2])
    return max(dp1_max, dp2_max)
