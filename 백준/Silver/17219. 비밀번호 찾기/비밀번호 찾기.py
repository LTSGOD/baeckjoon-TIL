import sys

input = sys.stdin.readline

N, M  =map(int, input().split())

book = dict()

for _ in range(N):
    a,b = input().rstrip().split()
    book[a] = b

for _ in range(M):
    q = input().rstrip()

    print(book[q])