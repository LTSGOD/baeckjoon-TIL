def updateIndex(array,인덱스):
    while array[인덱스] == 0:
        인덱스 -= 1
        if 인덱스 < 0:
            return 0
    return 인덱스

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    배달인덱스 = updateIndex(deliveries, len(deliveries) - 1)
    픽업인덱스 = updateIndex(pickups, len(pickups) - 1)
    
    #거리 계산
    #종료조건 반례 24 0 0 0  24 0 0 0같은 수 남았을 때 그냥 종료
    #그냥 인덱스가 둘다 0과 같아지면 종료하게 했는데 그러면 위와같은 반례
    while 배달인덱스 != 0 or 픽업인덱스 !=0 or deliveries[0] != 0 or pickups[0] > 0:
        #둘중 긴거리로 업데이트
        answer += (max(배달인덱스, 픽업인덱스) + 1) * 2
        
        용량 = cap
        while 용량 > 0:
            if 배달인덱스 == 0 and deliveries[배달인덱스] == 0:
                break
                
            최소값 = min(deliveries[배달인덱스], 용량)
            deliveries[배달인덱스] -= 최소값
            용량 -= 최소값
            배달인덱스 = updateIndex(deliveries, 배달인덱스)

        용량 = cap
        while 용량 > 0:
            if 픽업인덱스 == 0 and pickups[픽업인덱스] == 0:
                break
            최소값 = min(pickups[픽업인덱스], 용량)
            pickups[픽업인덱스] -= 최소값
            용량 -= 최소값
            픽업인덱스 = updateIndex(pickups, 픽업인덱스)
        # print(배달인덱스, 픽업인덱스)
        # print(deliveries, pickups)
        # print(answer)
    return answer