def check(stones,mid, k):
    
    count = 0 
    
    for i in range(0, len(stones)):
        if stones[i] - mid < 1:
            count += 1
        else:
            count = 0
        
        if count == k:
            return False
    return True
def solution(stones, k):
    answer = 0
    
    start = 0
    end = max(stones)
    
    while start + 1 < end:
        
        mid = (start + end) // 2
        
        #건널수있다 T
        #건널수없다 F
        if check(stones, mid, k):
            start = mid
        else:
            end = mid
            
    return start + 1