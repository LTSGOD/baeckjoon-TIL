def solution(routes):
    answer = 1
    
    #진입순서로 정렬했는데 진출순서로 정렬해야했음.
    routes.sort(key=lambda x: x[1])
    
    기준 = routes[0][1]
    
    i = 1
    while i < len(routes):
        if routes[i][0] > 기준:
            기준 = routes[i][1]
            answer+=1
        i += 1
    return answer