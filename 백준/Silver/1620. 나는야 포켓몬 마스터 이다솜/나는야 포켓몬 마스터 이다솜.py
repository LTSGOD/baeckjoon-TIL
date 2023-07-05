import sys

input = sys.stdin.readline

N, M = map(int, input().split())

poketmon = [input().rstrip() for i in range(N)]
poketmon_dict = {name: i+1 for i, name in enumerate(poketmon)}

questions = [input().rstrip() for i in range(M)]

for q in questions:
    if q.isdigit():
        print(poketmon[int(q)-1])
    else:
        print(poketmon_dict[q])
