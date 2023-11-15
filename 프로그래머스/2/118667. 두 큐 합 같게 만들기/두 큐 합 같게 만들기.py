from collections import deque

def solution(queue1, queue2):
    
    # 1 1
    # 1 5
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # sum을 while에서 계속돌리니까 시간초과
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    len_q = len(queue1)
    
    answer = 0
    
    flag = False
    
    i = 0
    while (i < len_q * 3):

        #q1 이 크면 
        if sum_q1 > sum_q2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum_q1 -= tmp
            sum_q2 += tmp
            answer+=1
        #q2 가 크면
        elif sum_q1 < sum_q2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_q1 += tmp
            sum_q2 -= tmp
            answer+=1
        else:
            flag = True
            break
        i += 1

        
    if flag: 
        return answer
    else:
        return -1
    
    
    
    