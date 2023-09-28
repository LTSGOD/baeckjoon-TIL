import sys
from copy import deepcopy

input = sys.stdin.readline


#전체를 브루트 포스로 하면 2의 49승으로 시간초과가 날 것 같긴함.
# 근데 2초니까 되지 않을까??
# 1초에 약 10에 9승 정도
#역시 시간초과

# A, B의 갯수를 고정하고 브루트포스를 돌자
#역시 시간초과

# S->T 가 아닌 T -> S에서 찾으면 시간을 더 절약 가능

S = input().rstrip()

T = input().rstrip()

def recursion(string):
    if len(string) == len(S):
        if string == S:
            print(1)
            exit()
        return

    if string[-1] == "A":
        recursion(string[:-1])
    if string[0] =="B":
        recursion(string[1:][::-1])

recursion(T)
print(0)
#---------------------------그냥 브루트 포스-----------

# def recursion(string, length):
#     if length == len(T):
#         print(string)
#         if string == T:
#             print(1)
#             exit()
#         return

#     A = string +"A"
#     # print(f'A {A}')
#     recursion(A, length+1)


#     tmp = string + "B"
#     B = "".join([tmp[i]for i in range(length, -1, -1)])

#     # print(f'B {B}')
#     recursion(B, length + 1)


# ---------------------------A B갯수 고정------------

#def recursion(string, info, length):
#     if length == len(T):
#         # print(string)
#         if string == T:
#             print(1)
#             exit()
#         return
    
#     for i, num in enumerate(info):
        
#         #붙여야할 A,B가 존재한다면
#         if num > 0:
#             # tmp 는 넘겨줄 string 변수
#             tmp = 0
#             if i == 0:
#                 tmp = string+"A"
#             elif i == 1:
#                 tmp = (string +"B")[::-1]

#             info_c = deepcopy(info)
#             info_c[i] -= 1
#             recursion(tmp,info_c,length+1)

# info = [T.count("A") - S.count("A"), T.count("B") - S.count("B")]