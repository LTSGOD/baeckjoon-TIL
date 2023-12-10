
def check(times,mid,n):
    #mid 는 시간
    result = 0
    for t in times:
        result += (mid // t)
    
    if result >= n:
        return True
    else:
        return False
def solution(n, times):
    
    #어려웠던 것 예시에 나온 상황(심사대가 비지만 기다리는 경우)을
    # 28 / 7 + 28/10 으로 퉁쳐도 되는지
    #1 10000000000
    
    start = 0
    end = max(times) * n
    
    while start + 1 < end:
        
        mid = (start + end) // 2
        
        if check(times, mid, n):
            end = mid
        else:
            start = mid
    return end