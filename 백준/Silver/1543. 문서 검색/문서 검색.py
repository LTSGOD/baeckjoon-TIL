import sys
from collections import deque
input = sys.stdin.readline

document = input().rstrip()

query = input().rstrip()

q_len = len(query)
i = 0
count = 0
while i < len(document)-q_len+2:
    tmp = document[i:i+q_len]
    if tmp == query:
        count += 1
        i += q_len
    else:
        i +=1

print(count)