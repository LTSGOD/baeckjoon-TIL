#dlru
#모든경우 판단해보고 출력
import sys
sys.setrecursionlimit(10 ** 8)

def recursion(depth,n,m,current_x,current_y,r,c, k):
    if depth == k:
        if current_x == r and current_y == c:
            return True
        return False
    
    #현재 있는 거리에서 더이상 도착지에 갈 수 없다면
    if abs(r-current_x)+ abs(c - current_y) > (k - depth):
        return False

    #판단해주기
    if ((k-depth) - abs(r-current_x) - abs(c-current_y)) % 2 != 0:
        return False
    
    for d in ['d','l','r','u']:
        
        #경계 벗어나는경우
        if d == 'd':
            if current_x + 1 > n:
                continue
            else:
                current_x += 1
        elif d =='l':
            if current_y - 1 < 1:
                continue
            else:
                current_y -= 1
        elif d== 'r':
            if current_y + 1 > m:
                continue
            else:
                current_y += 1
        else:
            if current_x - 1 < 1:
                continue
            else:
                current_x -= 1
        
        result.append(d)
        if recursion(depth+1, n,m, current_x, current_y,r,c,k):
            return True
        result.pop()
        
        if d == 'd':
            current_x -= 1
        elif d == 'l':
            current_y += 1
        elif d == 'r':
            current_y -= 1
        else:
            current_x += 1
        
def solution(n, m, x, y, r, c, k):
    answer = ''
    global result
    result = []

    recursion(0,n,m,x,y,r,c,k)
    
    if not result:
        return "impossible"
    else:
        return "".join(result)
    
    return "".join(result)
