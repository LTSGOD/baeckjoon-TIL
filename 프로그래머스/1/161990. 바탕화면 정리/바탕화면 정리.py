def top_x(wallpaper):
    for i,line in enumerate(wallpaper):
        for j, file in enumerate(line):
            if file == "#":
                
                return i

def top_y(wallpaper):
    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":      
                return i
def bottom_x(wallpaper):
    for i in range(len(wallpaper)-1,-1,-1):
        for j in range(len(wallpaper[0])-1, -1, -1):
            if wallpaper[i][j] == "#":
                
                return i + 1
def bottom_y(wallpaper):
    for j in range(len(wallpaper[0])-1,-1,-1):
        for i in range(len(wallpaper)-1, -1, -1):
            if wallpaper[i][j] == "#":
                
                return j + 1

def solution(wallpaper):
    answer = []
    
    answer.append(top_x(wallpaper))
    answer.append(top_y(wallpaper))
    answer.append(bottom_x(wallpaper))
    answer.append(bottom_y(wallpaper))
    #왼쪽 위 밑 오른쪽 완탐
    
    
    return answer