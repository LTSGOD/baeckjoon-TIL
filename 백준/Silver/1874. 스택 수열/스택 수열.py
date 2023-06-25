import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

stack = deque()
result = []

count = 1
flag = False
for num in l:
    while(count <= num):
        stack.append(count)
        count += 1
        result.append('+')
    if(stack.pop() != num):
        print("NO")
        flag = True
        break
    else:
        result.append('-')

if(flag == False):
    for a in result:
        print(a)

