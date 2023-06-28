import sys
import math
input = sys.stdin.readline


def check(num):
    tmp = math.floor(num)
    if(num < tmp + 0.5):
        return math.floor(num)
    else:
        return math.ceil(num)


n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

delete_n = check(n * 0.15)
l.sort()

if(n == 0):
    print(0)
elif(n < 4):
    print(check(sum(l)/len(l)))
else:

    result = l[delete_n:-delete_n]
    mean = check(sum(result) / len(result))

    print(mean)
