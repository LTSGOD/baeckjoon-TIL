import math
def solution(fees, records):
    현재주차장 = {}
    정산관리 = {}
    answer = []
    
    for record in records:
        시간, 번호, 출입 = record.split()
        
        시, 분 = 시간.split(":")
        시간 = int(시) * 60 + int(분)
        
        #들어오면 현재주차장에 저장
        if 출입 == "IN":
            현재주차장[번호] = 시간
            
        #나가면 정산부에다가 있었던 시간 저장
        else:
            if 정산관리.get(번호):
                정산관리[번호] =  정산관리[번호] + (시간 - 현재주차장[번호])
            else:
                정산관리[번호] = (시간 - 현재주차장[번호])
            현재주차장.pop(번호)
        
    #아직 나가지 않는 차량 체크
    for k in 현재주차장.keys():
        if 정산관리.get(k):
            정산관리[k] += (1439-현재주차장[k])
        else:
            정산관리[k] = (1439-현재주차장[k])

    정렬키 = sorted(정산관리.keys())
    
    for 키 in 정렬키:
        if 정산관리[키] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((정산관리[키] - fees[0]) /fees[2])) * fees[3])
    return answer