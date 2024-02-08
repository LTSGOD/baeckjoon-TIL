def check(rocks, mid, n):
    
    count = n
    기준 = rocks[0]
    
    for i in range(1, len(rocks)):
        
        # 바위 바위 사이 거리
        d = rocks[i] - 기준
        
        # 0  2 3 4  5   10

        # 0 2 11 14 17 21
        
        #최대거리 제시값인 최솟값mid 보다 작다면
        if d < mid:
            
            #근데 더이상 돌을 뺄 수 없으면 그것은 최솟값 만족 X
            if count == 0:
                return False
            else:
                count -= 1
        else:
            기준 = rocks[i]
    
    print("count", count)
    
    return True
            

def solution(distance, rocks, n):
    answer = 0
    
    start = 0
    end = distance
    
    rocks.sort()
    

    rocks = [0] + rocks + [end]
        

    #문제 없이 최댓 값이다 - > T
    # T T T T T F F F F 
    # 멈췄을때 왼쪽이 최댓값
    while start + 1 < end:

        mid = (start + end) // 2
        
        print(start, mid, end)
        
        if check(rocks, mid, n):
            start = mid
        else:
            end = mid
    # print(start, mid, end)
    
    #반례1. 모든 값이 T일때
    if start == distance - 1:
        return end
    else:
        return start
    
    
#반례
# 마지막 distance 추가 해줘야함
#	48, [0 12, 25, 38, 43], 1