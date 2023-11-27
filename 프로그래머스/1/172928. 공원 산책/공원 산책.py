def solution(park, routes):
    
    H = len(park)
    W = len(park[0])
    routes = [line.split() for line in routes]

    flag = False
    x = 0
    y = 0
    for i in range(H):
        if flag:
            break
        for j in range(W):
            if park[i][j] == "S":
                x = i
                y = j
                flag = True
                break

    for direction, num in routes:
        num = int(num)
        if direction == "N":
            for i in range(1,num+1):
                if x - i < 0 or park[x-i][y] == "X":
                    break
            else:
                x -= num
        elif direction == "E":
            for i in range(1,num+1):
                if y + i > W - 1 or park[x][y + i] == "X":
                    break
            else:
                y += num
        elif direction == "S":
            for i in range(1,num+1):
                if x + i > H - 1 or park[x+i][y] == "X":
                    break
            else:
                x += num
        elif direction == "W":
            for i in range(1,num+1):
                if y - i < 0 or park[x][y-i] == "X":
                    break
            else:
                y -= num
    return [x,y]