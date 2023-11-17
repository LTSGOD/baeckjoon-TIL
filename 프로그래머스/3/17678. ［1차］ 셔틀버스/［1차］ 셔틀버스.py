def cal(time):
    
    
    h = int(time[:2])
    m = int(time[3:])
    
    
    return h *60 + m


def timeToS(num):
    
    h = num // 60
    m = num % 60
    h = str(h)
    m = str(m)
    
    return h.zfill(2) + ":" + m.zfill(2)
    
def check(start, end, 확인시간,timetable,m):
    count = 0
    
    for crew_time in timetable:
        if (start < crew_time) and (end >= crew_time):
            
            if crew_time > 확인시간:
                if count < m:
                    return True
            else:
                count += 1
    return False
                    

def solution(n, t, m, timetable):
    
    answer = 0
    버스시간표 = [540 + (t * i) for i in range(n)]
    버스시간표.sort()
    
    timetable = [cal(tt) for tt in timetable]
    timetable.sort()
    # print(버스시간표)
    # print(timetable)
    
    i = 0
    for bus_time in 버스시간표:
        
        count = 0
        # print(bus_time, i)
        while i < len(timetable):
            if count == m:
                break
            if timetable[i] <= bus_time:
                count += 1
            else:
                break
            i += 1
        
        # print(f'count {count}')
        if count == m:
            answer = timetable[i-1] - 1
            # print("hoho")
        else:
            answer = bus_time
        #     print("haha")
        # print(answer)
    

    return timeToS(answer)