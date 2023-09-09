import sys

input = sys.stdin.readline

N = int(input())

check = dict()

for _ in range(N):
    name, abs = input().rstrip().split()

    if abs == "enter":
        check[name] = 1
    else:
        check.pop(name)

result = []
for key in check.keys():
    result.append(key)
result.sort(reverse=True)
for i in result:
    print(i)