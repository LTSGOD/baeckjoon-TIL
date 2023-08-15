from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    half = (sum(queue1) + sum(queue2)) // 2
    
    q1 = sum(queue1)
    q2 = sum(queue2)
    
    flag = False
    for element in queue1:
        if element > half:
            answer = -1
            flag = True
    for element in queue2:
        if element > half:
            answer = -1
            flag = True
    
    q1_len = len(queue1)
    if flag == False:
        queue1.extend(queue2)
        count = 0
        q1_start = 0
        q2_start = q1_len
        while(q1 != q2):
            if q1 > q2:
                if(q1_start > len(queue1) - 1):
                    q1_start = 0
                q1 = q1 - queue1[q1_start]
                q2 = q2 + queue1[q1_start]
                q1_start +=1
            else:
                if(q2_start > len(queue1) - 1):
                    q2_start = 0
                q1 = q1 + queue1[q2_start]
                q2 = q2 - queue1[q2_start]
                q2_start +=1
            count += 1
            if count > len(queue1) + 10:
                count = -1
                break
        answer = count
    
    return answer