import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N,M = map(int, input().split())

num = [i for i in range(1, N + 1)]

def recursion(num, next, depth):
    if depth == 0:
        for n in next:
            print(n,end=" ")
        print()
        return 


    for n in num:

        # num에서 n 선택해서 삭제
        copy_num = deepcopy(num)
        copy_num.remove(n)
        
        # print("-----------------")
        # print(copy_num)

        #next 복사 후 n 추가
        copy_next = deepcopy(next)
        copy_next.append(n)

        recursion(copy_num, copy_next, depth-1)

recursion(num, [], M)

