def solution(t, p):
    
    count = 0
    for i in range(len(t) - len(p) + 1):
        tmp = t[i:i+len(p)]
        if(int(tmp) <= int(p)):
            count+=1
    
    return count