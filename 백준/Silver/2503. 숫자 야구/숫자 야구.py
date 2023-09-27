import sys

input = sys.stdin.readline

N = int(input())



#가능성의 수를 모두 센뒤 해쉬에 저장 + 개수가 가장 높은것을 출력
# 가능한 조합에서 소거법? 
# 가능성있는 것은 소거법으로 추출하고 가능성있는것은 해쉬로 기억
# 계속 걸러내기 후보에서

pos_set = []
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            continue
        for k in range(1,10):
            if j == k:
                continue
            if i == k:
                continue
            pos_set.append([i,j,k])

for _ in range(N):
    query, target_strike,target_ball = map(int, input().split())

    a = query//100
    b = (query%100)//10
    c = (query%100)%10

    query = [a,b,c]
    tmp = []
    for answer in pos_set:
        strike = 0
        ball = 0
        #strike ball 판별
        for i in range(3):
            if query[i] == answer[i]:
                strike += 1
            else:
                if query[i] in answer:
                    ball += 1
        
        # target 스트라이크와 볼과 같으면 해쉬에 저장
        if strike == target_strike and ball == target_ball:
            tmp.append(answer)
    pos_set = tmp

print(len(pos_set))
# def one_ball(num):
#     a = num//100
#     b = (num%100)//10
#     c = (num%100)%10

#     candidate = []

#     num = [a,b,c]

#     for i,n in enumerate(num):

#         if n == a:
#             sub1 = b
#             sub2 = c
#         elif n == b:
#             sub1 = a
#             sub2 = c
#         else:
#             sub1 = a
#             sub2 = b

#         for s in pos_set:
#             # 해당하는 것만 candidate에 추가
#             if n not in s:
#                 continue
#             if s[i] == n:
#                 continue
#             if sub1 in s:
#                 continue
#             if sub2 in s:
#                 continue

#             candidate.append(s)
#         # print(len(candidate))
#     # print(candidate)
#     # print(len(candidate))

# def two_ball(num):
#     a = num//100
#     b = (num%100)//10
#     c = (num%100)%10

#     candidate = []

#     num = [a,b,c]

#     for i,n in enumerate(num):

#         if n == a:
#             sub1 = b
#             sub2 = c
#         elif n == b:
#             sub1 = a
#             sub2 = c
#         else:
#             sub1 = a
#             sub2 = b

#         for s in pos_set:
#             # 해당하는 것만 candidate에 추가
#             if n not in s:
#                 continue
#             if s[i] == n:
#                 continue
#             if sub1 in s:
#                 continue
#             if sub2 in s:
#                 continue

#             candidate.append(s)
# one_ball(123)
# print(len(pos_set))