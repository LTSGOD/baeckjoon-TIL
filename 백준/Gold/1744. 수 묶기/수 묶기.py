import sys
input = sys.stdin.readline

# N 최대 50
# 모든 경우의 수 탐색시
# 50C2 * 48C2 *

#정렬 nlogn
# 그후 n에 처리

# -10 -5 -4 -1 0 5 10 110
# 정렬 후
# 일단 음수 ~ 0 리스트
# 양수 리스트

#예외 사항 -> 중복해서 들어올 수 있다.
# 1 1 

# -5 -4 -1 -1 -1 0 1 1 1 5 5 

N = int(input())

minus = []
plus = []

for _ in range(N):
    tmp = int(input())

    if tmp <= 0:
        minus.append(tmp)
    else:
        plus.append(tmp)


minus.sort()
plus.sort(reverse=True)

result = 0


for i in range(0,len(minus),2):

    # print(f'i {i}')

    #홀수로 minus가 남는다면
    if i == len(minus) - 1:
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

for i in range(0,len(plus),2):

    if i == len(plus) -1:
        result += plus[i]
    else:
        곱 = plus[i] * plus[i+1]
        합 = plus[i] + plus[i+1]
        결과 = 0
        if 곱 > 합:
            결과 = 곱
        else:
            결과 = 합
        result += (결과)

# print(minus)
# print(plus)

print(result)

