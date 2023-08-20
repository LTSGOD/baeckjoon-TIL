import sys

input = sys.stdin.readline

N = int(input())
INF = int(1e9)
result = 0

nums = []
for _ in range(N):
    a, b = map(int, input().split())
    nums.append((a,b))
nums.sort()

start, end = nums[0][0], nums[0][1]

for i in range(1, N):
    a, b = nums[i][0], nums[i][1]
    
    if a <= end:
        end = end if end > b else b
        continue
    else:
        result += (end - start)
        start = a
        end = end if end > b else b
result += (end - start)

print(result)
