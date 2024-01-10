def recursion(n, start, end):
    
    if n == 1:
        answer.append([start, end])    
        return
    나머지 = abs(6 - start - end)

    recursion(n-1, start, 나머지)
    answer.append([start, end])
    recursion(n-1, 나머지, end)

def solution(n):
    global answer
    answer = []
    recursion(n, 1, 3)
    return answer