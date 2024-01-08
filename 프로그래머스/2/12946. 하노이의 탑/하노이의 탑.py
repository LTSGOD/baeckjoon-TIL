def recursion(n, to, end):
    
    if n == 1:
        answer.append([to, end])    
        return
    나머지 = abs(6 - to - end)

    recursion(n-1, to, 나머지)
    answer.append([to, end])
    recursion(n-1, 나머지, end)

def solution(n):
    global answer
    answer = []
    recursion(n, 1, 3)
    return answer