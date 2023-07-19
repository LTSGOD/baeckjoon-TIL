import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

book = {}
for _ in range(N):
    name, password = input().split()
    book[name] = password

for _ in range(M):
    print(book[input().rstrip()])