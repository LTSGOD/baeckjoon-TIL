import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

num_l = [i for i in range(1, n+1)]
stack = deque()

count = 1
i = 0
result = []
flag = False

stack.append(1)
result.append('+')
while i != n:
    # if(not stack):
    #     stack.append(num_l[count])
    #     result.append('+')
    #     count += 1

    if(stack[-1] == l[i]):
        stack.pop()
        result.append('-')
        i += 1
        # print(stack)
        # print(i)
        # print()
        if((not stack) and (i != n)):
            stack.append(num_l[count])
            result.append('+')
            count += 1
        continue
    elif(stack[-1] > l[i]):
        print('NO')
        flag = True
        break

    stack.append(num_l[count])
    result.append('+')
    count += 1
    # print(f'stack{stack}')
    # print(f'result{result}')

# print(stack)
if(flag == False):
    for i in result:
        print(i)

    # tmp = stack[-1]
    # num = l[i]
    # print(num)
    # print(tmp)
    # if(num > tmp):
    #     stack.append(num_l[count])
    #     result.append('+')
    #     count += 1
    # elif(num == tmp):
    #     i += 1
    #     result.append('-')
    #     stack.pop()
    # print(f'stack {stack}')
    # print(f'result {result}')

# if(i == n):
#     print(result)
# else:
#     print("NO")
