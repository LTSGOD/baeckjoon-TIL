def solution(targets):
    answer = 1
    
    targets.sort(key = lambda x : x[1])
    
    standard_s = targets[0][0]
    standard_e = targets[0][1]
    
    i = 1
    while i < len(targets):
        
        start = targets[i][0]
        end = targets[i][1]
        if start >= standard_e:
            standard_s = start
            standard_e = end
            answer += 1
        i += 1
    
    # print(targets)
    return answer