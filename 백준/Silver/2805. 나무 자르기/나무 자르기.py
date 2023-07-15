import sys


N, M = map(int, input().split())

trees = sorted(list(map(int, input().split())), reverse=True)


def check(n):
    count = 0
    for i in trees:
        if(i >= n):
            count += i - n
        else:
            continue
    return count


start = 0
end = N - 1

start = 0
end = max(trees)

while(start < end - 1):
    mid = (start + end) // 2
    if(check(mid) >= M):
        start = mid
    else:
        end = mid
print(start)
