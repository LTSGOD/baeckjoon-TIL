import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N ,x, y = map(int, input().split())

    flag = False
    while x <= N * M:
        if x % N == y % N:
            flag = True
            break
        x += M
    if flag:
        print(x)
    else:
        print(-1)