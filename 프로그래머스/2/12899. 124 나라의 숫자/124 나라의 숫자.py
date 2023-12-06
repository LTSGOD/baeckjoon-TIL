from collections import deque

def solution(n):
    result = deque()
    
    num = ["1","2","4"]
    while n > 0:
        n = n - 1
        
        result.appendleft(num[n % 3])
        n = n // 3
        
    return ''.join(list(result))