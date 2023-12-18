global picks

def recursion(depth, picks, N, minerals):
    global 최소피로도
    if depth == N:
        # print(result)
        피로도 = 캐기(minerals)
        # print(피로도)
        if 최소피로도 > 피로도:
            최소피로도 = 피로도
        return
    

    for 곡괭이번호 in [0,1,2]:
        if picks[곡괭이번호] == 0:
            continue

            
        #곡괭이 1개 빼기
        picks[곡괭이번호] -= 1
        # visited[곡괭이번호] = True
        result.append(곡괭이번호)
        
        recursion(depth+1, picks,N,minerals)
        
        picks[곡괭이번호] += 1
        result.pop()

def 캐기(minerals):
    
    점수표 = [[1,1,1],[5,1,1],[25,5,1]]
    answer = 0
    광물순서 = 0
    for 곡괭이번호 in result:
        count = 0 
        while 광물순서 < len(minerals):
            #탈출조건
            if count > 4:
                break
            #광물점수표로 계산위한 광물인덱스 산출    
            광물인덱스 = 0
            if minerals[광물순서] == "diamond":
                광물인덱스 = 0
            elif minerals[광물순서] == "iron":
                광물인덱스 = 1
            else:
                광물인덱스 = 2
            
            #결과에 피로도 더하기
            # print(점수표[곡괭이번호][광물인덱스])
            answer += 점수표[곡괭이번호][광물인덱스]
            count += 1
            광물순서 += 1
    return answer
def solution(picks, minerals):
    global result
    global 최소피로도
    최소피로도 = int(1e9)
    
    최대곡괭이 = len(minerals) // 5 + 1
    result = []
    print(최대곡괭이)
    
    #시간초과로 min 조건 추가
    recursion(0, picks, min(최대곡괭이, sum(picks)), minerals)
    return 최소피로도