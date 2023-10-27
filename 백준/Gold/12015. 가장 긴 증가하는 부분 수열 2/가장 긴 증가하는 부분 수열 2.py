import sys
input = sys.stdin.readline


# 중복 없이 정렬 시키고 합 하면 되지 않나?
# 안됨
# 예외 10 20 10 30 20 12 50 11 13 14

#10 12 13 14 50 51
#원래는 DP를 이용하면 최장수열의 원소도 구할 수 있음
# 시간 복잡도 n2

#하지만 시간 복잡도를 줄이고 길이만 알려 하면 nlogn으로 줄일 수 있다.

N = int(input())

수열 = list(map(int, input().split()))

result = [수열[0]]

for i, n in enumerate(수열):
    if i == 0:
        continue

    #담는 배열의 마지막보다 n이 크다면 그냥 append
    if result[-1] < n:
        result.append(n)
    #아닌경우 이진탐색해서 처음 같거나 큰 수 자리에 대체
    else:
        start = 0
        end = len(result) - 1
        # print(f"-----------{n}--------------")
        # print(result)
        # print(start, end)
        while start + 1 < end:

            mid = (start + end) // 2

            if result[mid] < n:
                start = mid
            else:
                end = mid

            # print(start, end, mid)
        # print(start, end)
        if result[start]  >= n:
            result[start] = n
        else:
            result[end] = n
        # print(f'result {result}')

# print(result)
print(len(result))