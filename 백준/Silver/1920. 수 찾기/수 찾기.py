import sys

input = sys.stdin.readline

N = int(input())

AN = list(map(int, input().split()))

M = int(input())

query = list(map(int, input().split()))

book = dict()

for A in AN:
    book[A] = 0

for q in query:
    if book.get(q) != None:
        print(1)
    else:
        print(0)