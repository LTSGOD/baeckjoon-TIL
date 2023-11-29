def solution(dirs):
    answer = 0
    
    신기한방문사전 = dict()
    x = 0
    y = 0
    for d in dirs:
        
        if d == "U":
            #범위 넘어가면 pass
            if y + 1 > 5:
                continue
            key = f"{x}{y}{x}{y+1}"
            key2 = f"{x}{y+1}{x}{y}"
            #출발 도착이 아직 사전에 없으면 추가
            if 신기한방문사전.get(key) is None:
                신기한방문사전[key] = 1
                신기한방문사전[key2] = 1
                answer += 1
            y += 1
        elif d == "D":
            #범위 넘어가면 pass
            if y - 1 < -5:
                continue
            key = f"{x}{y}{x}{y-1}"
            key2 = f"{x}{y-1}{x}{y}"
            
            #출발 도착이 아직 사전에 없으면 추가
            if 신기한방문사전.get(key) is None:
                신기한방문사전[key] = 1
                신기한방문사전[key2] = 1
                answer += 1
            y -= 1
        elif d == "R":
            #범위 넘어가면 pass
            if x + 1 > 5:
                continue
            key = f"{x}{y}{x+1}{y}"
            key2 = f"{x+1}{y}{x}{y}"
            
            #출발 도착이 아직 사전에 없으면 추가
            if 신기한방문사전.get(key) is None:
                신기한방문사전[key] = 1
                신기한방문사전[key2] = 1
                answer += 1
            x += 1
        elif d == "L":
            #범위 넘어가면 pass
            if x - 1 < -5:
                continue
            key = f"{x}{y}{x-1}{y}"
            key2 = f"{x-1}{y}{x}{y}"
            
            #출발 도착이 아직 사전에 없으면 추가
            if 신기한방문사전.get(key) is None:
                신기한방문사전[key] = 1
                신기한방문사전[key2] = 1
                answer += 1
            x -= 1
    
    return answer
