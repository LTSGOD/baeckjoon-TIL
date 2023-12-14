from collections import deque
def solution(order):
    answer = 0
    
    보조컨베이어 = []
    
    주컨베이어 = deque([i+1 for i in range(len(order))])
    
    i = 0
    
    while True:
        
        
        #주컨베이어 체크
        if 주컨베이어 and (order[i] == 주컨베이어[0]):
            answer += 1
            주컨베이어.popleft()
            i += 1
        else:
            #보조컨베이어 체크
            if 보조컨베이어 and (order[i] == 보조컨베이어[-1]):
                보조컨베이어.pop()
                answer += 1
                i+=1
            else:
                
                #만약 보조다 옮겼는데 주컨베이어 비어있으면
                if not 주컨베이어:
                    break
                else:
                    tmp = 주컨베이어.popleft()
                    보조컨베이어.append(tmp)
    
    
    return answer