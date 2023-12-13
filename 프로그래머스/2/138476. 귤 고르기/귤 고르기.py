def solution(k, tangerine):
    answer = 0
    신기한귤사전 = dict()
    
    #귤종류별 갯수 세기
    for t in tangerine:
        if 신기한귤사전.get(t) is None:
            신기한귤사전[t] = 1
        else:
            신기한귤사전[t] += 1
    
    #리스트 변환
    신기한귤사전 = [[key, 신기한귤사전[key]]for key in 신기한귤사전]
    
    #정렬
    신기한귤사전.sort(key=lambda x: x[1], reverse=True)
    
    #귤담기
    귤바구니 = 0
    for 귤종류, 귤갯수 in 신기한귤사전:
        귤바구니 += 귤갯수 
        answer += 1
        if 귤바구니 >= k:
            return answer
    # print(신기한귤사전)
    return answer