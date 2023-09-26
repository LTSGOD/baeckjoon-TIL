import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

A = deque(map(int, input().split()))

operator = list(map(int, input().split()))

def recursion(A, operator, operator_num):
    global min_v 
    global max_v 

    if operator_num == 0:
        if A[0] > max_v:
            max_v = A[0]
        
        if A[0] < min_v:
            min_v = A[0]
        # print(A[0])

        return A

    # print(A, operator)

    for i,o in enumerate(operator):
        if o > 0:

            #다음 연산자 토스
            next_operator = deepcopy(operator)
            next_operator[i] -= 1

            # 숫자 계산
            next_num = deepcopy(A)
            a = next_num.popleft()
            b = next_num.popleft()
            tmp = 0

            if i == 0:
                tmp = a + b
            elif i == 1:
                tmp = a - b
            elif i == 2:
                tmp = a*b
            else:
                #혹시 문제 발생시 나눗셈 수정
                # tmp = a//b -> -1 // 3 == -1 의 결과 나옴
                if a < 0 and b > 0:
                    tmp = abs(a) // b
                    tmp = -tmp
                else:
                    tmp = a//b

            #다음 숫자 배열 토스
            next_num.appendleft(tmp)

            recursion(next_num,next_operator,operator_num-1)

# global min_v 
# min_v = int(1e8)
# global max_v 
# max_v = 0

#범위가 10억이라 int(1e8하면 안됨.)
min_v = int(1e9)
#초기 0으로 설정해서 -값이 최대일경우 무시됨. 
max_v = -int(1e9)+1

recursion(A, operator, sum(operator))

print(max_v)
print(min_v)