import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
pN = input().rstrip()

length = 2*n + 1
correct = ""
for i in range(length):
    if i % 2 == 0:
        correct += 'I'
    else:
        correct += 'O'
count = 0

for i, string in enumerate(pN):
    if string == 'I':
        if i +length > m:
            break
        tmp = pN[i:i+length]
        if tmp == correct:
            count += 1
print(count)