import sys

input = sys.stdin.readline

N = int(input())

stack = []


def recursion(n, start, end):
    if n == 1:
        print(start, end)
        return

    m = 6 - start - end
    recursion(n-1, start, m)
    print(start, end)
    recursion(n-1, m, end)


print(2**N-1)
if(N <= 20):
    recursion(N, 1, 3)
