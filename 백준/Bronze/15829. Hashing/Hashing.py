import sys

input = sys.stdin.readline

n = int(input())

string = input().rstrip()

result = 0

for i, s in enumerate(string):
    tmp = ord(s) - 96
    result += ((tmp * pow(31,i))%1234567891)

print(result%1234567891)