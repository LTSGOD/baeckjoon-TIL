import sys
from collections import deque
input = sys.stdin.readline

N = int(input())


#################### 재귀 풀이 #######################
array = list(map(int, input().split()))

level = [[] for _ in range(N)]

def recursion(arr, depth):
    if depth > N - 1:
        return

    mid = len(arr) // 2
    level[depth].append(arr[mid])
    recursion(arr[:mid], depth + 1)
    recursion(arr[mid:], depth + 1)

recursion(array, 0)

for l in level:
    for s in l:
        print(s,end=" ")
    print()


################## 재귀 X 풀이 ####################
# array = deque(map(int, input().split()))

# array.appendleft(0)

# mid = len(array)//2

# result = deque()
# i = 1
# j = 2
# while i <= mid:
#     tmp = []
#     for index in range(i, len(array), j):
#         tmp.append(array[index])
#     j *= 2
#     i *= 2
#     result.appendleft(tmp)

# for l in result:
#     for s in l:
#         print(s,end=" ")
#     print()