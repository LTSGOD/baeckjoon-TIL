import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

def recursion(num):
    if num == 1:
        return A
    mid = num // 2

    if num % 2 == 0:
        return ((recursion(mid) % C) ** 2) %C
    else:
        return ((((recursion(mid) % C) ** 2)%C) *A) % C

print(recursion(B)% C)