# ex) 9  4개
# 끄아 너무 어려워;;

def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    공평하게나눠가지는수 = s//n
    
    #이수는 항상 n 보다 작음
    안나누어떨어지면더해야하는수 = s%n
    
    for i in range(n):
        answer.append(공평하게나눠가지는수)
    
    if 안나누어떨어지면더해야하는수 != 0:
        
        for i in range(n):
            answer[i] += 1
            안나누어떨어지면더해야하는수 -= 1
            
            if 안나누어떨어지면더해야하는수 == 0:
                break
    answer.sort()
    return answer