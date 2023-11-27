max_plus = 0
max_money = 0

def discount(num, ratio):
    return num * (1.0-(ratio/100))

def check(users, 이모티콘):
    
    플러스가입자수 = 0
    총가격합 = 0
    for 비율기준, 가격기준 in users:
        가격합 = 0
        for 비율, 가격 in 이모티콘:
            if 비율 >= 비율기준:
                가격합 += 가격
                
        if 가격합 >= 가격기준:
            플러스가입자수 += 1
        else:
            총가격합 += 가격합
            
    return 플러스가입자수, 총가격합

def recursion(depth, users, N):
    global max_plus
    global max_money
    
    if depth == N:
        이모티콘 = [[ratio[i],discount(price,ratio[i])] for i,price in enumerate(emo)]
        plus, money = check(users, 이모티콘)
        if plus > max_plus:
            max_plus = plus
            max_money = money
        elif (plus == max_plus) and (money > max_money):
            max_money = money
        return
        
    for r in [40,30,20,10]:
        ratio.append(r)
        recursion(depth+1, users ,N)
        ratio.pop()
        
def solution(users, emoticons):    
    global ratio
    global emo
    emo = emoticons
    ratio = []
    
    emoticons.sort()

    recursion(0, users, len(emoticons))
    
    
    return [max_plus, max_money]