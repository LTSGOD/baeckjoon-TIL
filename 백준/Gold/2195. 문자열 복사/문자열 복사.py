import sys
from collections import deque
input = sys.stdin.readline


S = input().rstrip()

P = input().rstrip()
P_len = len(P)
S_len = len(S)

i = 0
result = 0
while i < P_len:
    max_count = 0
    for j in range(1, P_len - i + 1):
        if P[i:i+j] in S:
            max_count = j
        else:
            break
    result +=1
    i += max_count

print(result)











# i = 0
# result = 0

# #xy0zy0x
# #zzz0yyy0xxx
# print(S_len)
# while i < P_len:
#     j = 0
#     max_len = 1
#     count = 0
#     tmp = i
#     while j < S_len:
#         if P[tmp] == S[j]:
#             count += 1
#             tmp += 1
#             if tmp == P_len:
#                 break
#         else:
#             if count != 0:
#                 max_len = count
#                 count = 0
#             tmp = i
#         j += 1
#     result += 1
#     i += max_len

# print(result)