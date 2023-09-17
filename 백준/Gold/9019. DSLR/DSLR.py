import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def L(num):
    tmp = str(num)
    length = len(tmp)
    prefix = '0' * (4-length)
    tmp = prefix + tmp
    tmp = tmp[1:] + tmp[0]
    return int(tmp)

def R(num):
    tmp = str(num)
    length = len(tmp)
    prefix = '0' * (4-length)
    tmp = prefix + tmp
    tmp = tmp[-1] + tmp[:-1]
    return int(tmp)

def D(num):
    return (2 * num) % 10000

def S(num):
    if num == 0:
        return 9999
    tmp = num -1
    return tmp

def bfs(num):
    q = deque()
    q.append((num,""))

    while q:
        current, commands = q.popleft()

        if current == B:
            return commands

        if visited[current] == True:
            continue
        
        left = L(current)
        q.append((left,commands+"L"))
        right = R(current)
        q.append((right,commands+"R"))
        down = D(current)
        q.append((down,commands+"D"))
        sub = S(current)
        q.append((sub,commands+"S"))

        visited[current] = True



for _ in range(T):
    A,B = map(int, input().split())
    visited = [False] * 10000
    print(bfs(A))