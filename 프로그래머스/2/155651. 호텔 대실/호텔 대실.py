from heapq import heappop, heappush, heapify

def translation(element):
    
    start = element[0]
    end = element[1]
    
    start = int(start[:2]) * 60 + int(start[3:])
    end = int(end[:2]) * 60 + int(end[3:])
    
    return [start, end]

def solution(book_time):
    answer = 1
    
    book_time = list(map(translation, book_time))
    
    #입실시간이 빠른 순서대로 현재 객실에서 가장 빨리 퇴실하는 친구들이 있는지 확인
    heapify(book_time)
    
    # 첫친구들은 무조건 대실 할 수 있으니 세팅
    입실, 퇴실 = heappop(book_time)
    현재객실상태 = []
    heappush(현재객실상태, (퇴실, 입실))
    
    # print(book_time)
        
    while book_time:
        
        입실, 퇴실 = heappop(book_time)
        
        퇴실시간 = 현재객실상태[0][0]
        
        #지금 입실하는 친구가 바톤터치해서 들어갈 수 있으면
        if 입실 >= 퇴실시간 + 10:
            heappop(현재객실상태)
        #없으면 방 추가
        else:
            answer += 1
        heappush(현재객실상태, (퇴실, 입실))
        # print(현재객실상태)
        
        
    
    return answer