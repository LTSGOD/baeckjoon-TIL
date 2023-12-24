from itertools import combinations

#False 인거 세기
def check(배열):
    count = 0
    result = []
    for i,b in enumerate(배열):
        if b == False:
            result.append(i)
            count += 1
    return result, count

#tuple이 서로 같은지 비교
def check2(relation, index, 중복체크, key, 후보키):
    global answer
    for r in relation:
        
        #변환
        튜플 = "".join([r[i] for i in index])
        
        if 중복체크.get(튜플):
            break
        else:
            중복체크[튜플] = 1
    else:
        # for i in index:
        #     key[i] = True
        answer += 1
        후보키.add(index)
        print("index", index)
    
    return 후보키

#최소성 검사
def check3(후보키, 인덱스):
    for 후보 in 후보키:
        for t in 후보:
            if t not in 인덱스:
                break
        else:
            return True        
    return False
    
def solution(relation):
    global answer
    answer = 0
    
    key = [False for _ in range(len(relation[0]))]
    컬럼 = [i for i in range(len(relation[0]))]
    후보키 = set()
    #조합별로
    for i in range(1, len(relation[0]) + 1):
        
#         #두번째에는 컬럼이 1개인거 제외
#         if i == 2:
#             컬럼, count = check(key)
        
#         #만약 뽑아야하는것보다 남은 것들이 적으면
#         # if count < i:
#         #     break
        for c in combinations(컬럼, i):
            
            #지금까지 검사한 후보키와 비교해서 최소성 검사
            if check3(후보키, c):
                continue

            중복체크 = dict()
            
            #후보키인지 체크
            후보키 = check2(relation, c, 중복체크, key, 후보키)
        # break
    print(key)
    return answer