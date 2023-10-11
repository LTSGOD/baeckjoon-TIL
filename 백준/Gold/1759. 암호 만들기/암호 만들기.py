import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

L, C = map(int,input().split())

alphabet = list(input().rstrip().split())
visited ={i:False for i in alphabet}

alphabet.sort()

def recursion(depth, result, start):
    global 모음
    global 자음

    if depth == L:
        if 모음 > 0 and 자음 > 1:
            print(''.join(result))
        return

    for i in range(start,C):

        if visited[alphabet[i]] == True:
            continue
        
        flag = True
        #모음이면 모음_condition True
        if alphabet[i] in ['a','e','i','o','u']:
            모음 += 1
        else:
            flag = False
            자음 += 1

        #result 리스트에 추가
        copy_result = deepcopy(result)
        copy_result.append(alphabet[i])

        visited[alphabet[i]] = True
        recursion(depth + 1, copy_result, i + 1)
        visited[alphabet[i]] = False
        if flag:
            모음 -= 1
        else:
            자음 -= 1

모음 = 0
자음 = 0
recursion(0,[], 0)