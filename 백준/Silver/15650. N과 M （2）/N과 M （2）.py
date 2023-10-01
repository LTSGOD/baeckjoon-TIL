import sys
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())

num = [i for i in range(1,N+1)]

visited = []

def recursion(num, M, result):
    if M == 0:
        result.sort()
        if result not in visited:
            for r in result:
                print(r, end=" ")
            print()
            visited.append(result)
        return

    for i,n in enumerate(num):
        num_copy = deepcopy(num)

        tmp = deepcopy(result)
        tmp.append(num_copy.pop(i))

        recursion(num_copy, M-1, tmp)


recursion(num, M, [])