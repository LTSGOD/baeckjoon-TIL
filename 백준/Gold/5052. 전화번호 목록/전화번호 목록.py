import sys

import heapq

input = sys.stdin.readline

T = int(input())

#그냥 정렬시 반례발견
#1
#2
#20
#2
# in 으로 체크 했더니 밑에 예시도 맡다고 표시... ㅠ 그래서 check 하는 함수 만듦
# 1
# 2
# 21
# 1

def check(current, b):
    # print("hoho")
    # print(current, b)
    for i in range(len(current)):
        if current[i] != b[i]:
            return False
    return True

for _ in range(T):

    # 전화번호 갯수 입력 받기
    N = int(input())

    number_list = []

    # 전화번호 갯수만 큼 number_list에 추가
    for _ in range(N):
        tmp = input().rstrip()

        number_list.append(tmp)
    
    # 왼쪽에 10자리를 채워서 오름차순 정렬 
    number_list.sort(key=lambda x: (x.ljust(10, '0'), len(x)))

    # heapq에 넣기 위해 인덱스 추가
    number_list = [(i, v) for i, v in enumerate(number_list)]

    #heapq화
    heapq.heapify(number_list)
    flag = True

    # print(number_list)

    #heapq에서 빼서 최소 값과 비교
    while number_list:

        #한개 꺼냄(최솟값 보장)
        _, current = heapq.heappop(number_list)
        
        #heapq가 비어있다면 멈춤
        if not number_list:
            break

        #꺼낸 값이 그 다음 값 안에 포함 되어있으면 일관성 X
        if check(current, number_list[0][1]):
            flag = False
            print('NO')
            break
    
    if flag:
        print('YES')

    # print(number_list)