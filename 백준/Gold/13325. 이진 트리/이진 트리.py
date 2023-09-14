import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

edge = deque(map(int, input().split()))

edge.appendleft(0)
edge.appendleft(0)

edge = [[i] for i in edge]

num = 2 ** (N+1) - 1

result = []

def max_recursion(index, level):
    if level == N:
        edge[index].append(edge[index][0])
        return edge[index][0]

    left = max_recursion(index * 2, level + 1)
    right = max_recursion(index*2+1,level+1)

    tmp = max(left, right)
    edge[index].append(tmp + edge[index][0])

    return tmp + edge[index][0]

def recursion(index, level, mvalue):
    if level == N:
        edge[index][0] = mvalue
        return
    if index != 0:
        tmp = mvalue - edge[index][1]
        edge[index][0] += tmp
    recursion(index*2, level + 1, mvalue - edge[index][0])
    recursion(index*2+1, level + 1,mvalue-edge[index][0])

max_recursion(1,0)

mvalue = edge[1][1]
recursion(1,0,mvalue)

result = 0
for i in range(2, num + 1):
    result += edge[i][0]
print(result)
#처음엔 최댓값을 찾고 밑에서부터 합쳐오는 방법을 생각. but 복잡
# def max_recursion(index, sum):
#     if index * 2 > num:
#         result.append(sum)
#         return

#     max_recursion(index * 2, sum + edge[index * 2])
#     max_recursion(index * 2 + 1, sum + edge[index * 2 + 1])

# def check(a, b):
#     count = 0
#     while a -count > 0 and b-count > 0:
#         count+=1
#     return count

# def max_recursion(index, level, sum):
#     if level == N:
#         return sum - edge[index]

#     left = max_recursion(index * 2, level + 1, sum + edge[index * 2])
#     right = max_recursion(index * 2 + 1,level+1, sum + edge[index * 2 + 1])

#     if level == N - 1:
#         tmp = check(mvalue - left - edge[index*2], mvalue - right - edge[index* + 1])
#         edge[index * 2] = left - tmp
#         edge[index* 2 + 1] = right - tmp
#         return edge[index] + tmp
#     elif level == 0:
#         edge[index * 2] = left
#         edge[index*2 + 1] = right
#         return
#     else:
#         tmp = check(left - edge[index*2], right - edge[index*2 + 1])
#         edge[index * 2] = left - tmp
#         edge[index * 2 + 1] = right - tmp
#         return tmp + edge[index]


# max_recursion(1, 0)


# tmp = sum(edge)

# mvalue = max(result)

# max_recursion(1,0,0)

# print(mvalue)
# print(edge)
# print(check)

