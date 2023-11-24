def solution(name, yearning, photo):
    answer = []
    
    그리움사전 = { name[i] : yearning[i] for i in range(len(name))}
    
    for i in range(len(photo)):
        
        그리움총합 = 0
        for n in photo[i]:
            if 그리움사전.get(n) is not None:
                그리움총합 += 그리움사전[n]
        answer.append(그리움총합)
    
    return answer