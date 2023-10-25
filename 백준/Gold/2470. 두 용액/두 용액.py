import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


# 일단 노가다로 모든 경우의 수를 계산할 경우
# O(n제곱) 시간복잡도 따라서 시간 초과
# nlong n 안에 끝내야함.


N = int(input())


attribute = list(map(int, input().split()))
attribute.sort()

result = []
for i,num in enumerate(attribute):

    attribute[i] = attribute[i-1]
    start = 0
    end = len(attribute) - 1
    # print(f'{num}----------------------------')
    # print(attribute[start], attribute[end])
    while start + 1 < end:

        #자기자신 선택되면 보정
        if start == i:
            start += 1
        if end == i:
            end -= 1

        mid = (start + end) // 2

        if num + attribute[mid] < 0:
            start = mid
        else:
            end = mid
        # print(attribute[start], attribute[end], attribute[mid])

    max_sum = 0
    if abs(num + attribute[start]) < abs(num +attribute[end]):
        max_sum = num+ attribute[start]
    else:
        max_sum = num+attribute[end]
    # print(f"append {(abs(max_sum),num ,max_sum-num)}")
    result.append((abs(max_sum), num, max_sum-num))

    attribute[i] = num

result.sort()
# print(f'result {result}')
answer = [result[0][1], result[0][2]]
answer.sort()
print(answer[0], answer[1])



#오름차순 정렬 후 
#check 조건 -> 숫자와 더한 후 -, + 의 경계선 탐색
# 그 후 절댓값이 작은 숫자 모음.

#-99 -2 -1 4 98

# -2 -1 4 98

#-99
# -101 -100 -95 -1


#98
# -1 96 97 102

#-2
# -101 -3 0 2 96

