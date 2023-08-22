import sys

input = sys.stdin.readline

# 비둘기집의 원리: 비둘기가 n마리가 집이 n-1개라면 반드시 한집에 2마리있는데가 있다.
# mbti 는 16개고 32개가 넘어가는 순간 3개 겹치는 mbti가 최소 1개는 나온다는 원리.
# 따라서 32개정도는 브루트포스로 풀어도 풀림.

T = int(input())

def check(a,b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)

    return len(a) - len(c)

for _ in range(T):
    N  = int(input())
    mbtis = input().rstrip().split()
    if N > 32:
        print(0)
        continue
    else:
        result = []
        for i in range(len(mbtis)-2):
            for j in range(i + 1, len(mbtis)-1):
                for k in range(j +1, len(mbtis)):
                    count = check(mbtis[i],mbtis[j])
                    count += check(mbtis[j], mbtis[k])
                    count += check(mbtis[i], mbtis[k])
                    result.append(count)
        result.sort()
        print(result[0])