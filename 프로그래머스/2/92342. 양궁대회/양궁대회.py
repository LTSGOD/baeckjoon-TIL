#경우의수
#n 최대 10
# 11C10 (1 * 10)
# 11C1 * 10C9 (2 * 1 1 * 9 선택)
# 3 1 1 1 1 1 1 1 (3 * 1 )
# 시간복잡도 계산하기 귀찬 완탐이 되지 않을까

#어피치점수, 라이언점수 계산
def check(라이언정보, 어피치정보, n):
    라이언점수 = 0
    어피치점수 = 0
    for i in range(11):
        
        if (라이언정보[i] == 0) and (어피치정보[i] == 0):
            continue
        elif 라이언정보[i] > 어피치정보[i]:
            라이언점수 += (10 - i)
        else:
            어피치점수 += (10- i)
    return 라이언점수, 어피치점수

#점수차가 같을 때 누가 낮은점수 맞았는지 비교 신규가 더 높다면 True 반환
def check2(기존, 신규):
    
    for i in range(10, -1, -1):
        if 신규[i] == 기존[i]:
            continue
        elif 신규[i] > 기존[i]:
            return 신규
        elif 신규[i] < 기존[i]:
            return 기존
        
def recursion(depth, n, info, index):
    global 최대점수차
    global 최고라이언정보
    
    if depth > n:
        return
    if depth == n:
        라이언점수, 어피치점수 = check(라이언정보, info, n)

        #어피치점수보다 클때
        if 라이언점수 > 어피치점수:
            
            #최대점수를 넘는다면
            if 라이언점수 - 어피치점수 > 최대점수차:
                최대점수차 = 라이언점수 - 어피치점수
                최고라이언정보 = [i for i in 라이언정보]
            #최대점수가 같을 때
            elif 라이언점수 - 어피치점수 == 최대점수차:
                
                #누가더 낮은 점수 많이 맞혔는지
                최고라이언정보 = [i for i in check2(최고라이언정보, 라이언정보)]
        return
    
    for i in range(index, len(라이언정보)):
        
        tmp = 0
        if i == 10:
            tmp = n - sum(라이언정보)
        else:
            tmp = info[i] + 1
        라이언정보[i] += tmp
        recursion(depth+tmp, n, info, i + 1)
        라이언정보[i] -= tmp

        
    
def solution(n, info):

    global 라이언정보
    global 최고라이언정보
    global 최대점수차
    최고라이언정보 = 0
    최대점수차 = -1
    라이언정보 = [0 for _ in info]
    
    recursion(0, n, info, 0)

    if 최고라이언정보 == 0:
        return [-1]
    else:
        return 최고라이언정보