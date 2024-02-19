from copy import deepcopy
from heapq import heappop, heappush
def comb(start, bucket, depth):
    
    if depth ==  (len(bucket)//2):
        tmp = [i for i in answer]
        dice_comb.append(tmp)
        return
    
    for i in range(start, len(bucket)):
        answer.append(i)
        comb(i+1, bucket, depth+1)
        answer.pop()

def perm(수,dice, depth, n, identify):
    global 승
    global 무
    global 패
    
    if depth == n:
        
        합 = sum(경우의수)

        if game[identify].get(합):
            game[identify][합] = game[identify][합] + 1
        else:
            game[identify][합] = 1

        return
    
    for num in dice[수[depth]]:
        경우의수.append(num)
        perm(수, dice, depth + 1, n, identify)
        경우의수.pop()

def cal(dice, 수):
    tmp =[]
    
    for i in dice:
        if i not in 수:
            tmp.append(i)
    return tmp
        
        
def solution(dice):
    global answer
    global dice_comb
    global 경우의수
    global game

    dice_index = [i for i in range(len(dice))]

    answer = []
    경우의수들 ={}
    경우의수 = []
    승패기록 = {}
    제발 = []
    
    #주사위 조합 찾기
    dice_comb = []
    comb(0, dice_index, 0)
    
    global 승
    global 무
    global 패
    #조합별 경우의 수 계산
    
    중복체크 = {}
    for 수 in dice_comb:
        승 = 0
        무 = 0
        패 = 0
        game = [{}, {}]
        
        #상대편 주사위 계산
        opposite = cal(dice_index, 수)
        
        mykey ="".join(list(map(str, 수)))
        oppkey = "".join(list(map(str, opposite)))
        
        if 중복체크.get(mykey):
            # print("ㅙㅗ")
            continue
            
        perm(수,dice, 0, len(수), 0)
        
        
        perm(opposite, dice, 0, len(opposite), 1)
        
        for 나 in game[0].keys():
            
            for 상대 in game[1].keys():
                
                if 나 > 상대:
                    승 += (game[0][나] * game[1][상대])
                elif 나 < 상대:
                    패 += (game[0][나] * game[1][상대])
                else:
                    무 += (game[0][나] * game[1][상대])
        
        if 승 > 패:
            heappush(제발, [-승, 수])
        else:
            # 제발.append([패, opposite])
            heappush(제발, [-패, opposite])
        
        중복체크[mykey] = 1
        중복체크[oppkey] = 1
        
        # print(수, 승, 무 , 패)

    return [i+1 for i in heappop(제발)[1]]