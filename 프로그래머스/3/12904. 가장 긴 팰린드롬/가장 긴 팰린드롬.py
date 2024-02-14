def solution(s):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for j in range(1, len(s) + 1):
        for i in range(j, len(s) + 1):
            a = s[j-1:i]
            b = a[::-1]
            # print(a, b)
            if a == b:
                if answer < len(a):
                    answer = len(a)

    return answer