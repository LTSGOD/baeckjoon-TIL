import math
# 1의 자리수 판단
# 올림 하는 것이 이득인지 버림하는 것이 이득인지

#6보다 작다면 버리는것이 이득이라고 생각
#그러나 95면 올리는 것이 이득
#그냥 둘다 구하고 비교?
#각자릿수마다 2가지 경우의 수를 모두 구해서 정답을 구함 2 9승 시간복잡도

#어려웠던것
#1. 버림수, 올림수 구하기
# 2. 반례를 머리로 이해하는것도 힘들었음
# 555, 678 

def recursion(num, depth, 합):
    global result
    # print("result",num, 합)
    if depth == 1:
        print("result", num, 합)
        #한자리수일경우
        if num < 10:
            합 = min(num, 10 - num + 1)
        else:
            일의자리 = int(str(num)[0])
            합 = 합 + min(일의자리, 10 - 일의자리 + 1)
        if 합 < result:
            result = 합
        return
    길이 = len(str(num)) + 1
    버림수 = math.floor(num / (10** (길이- depth)))* (10 **(길이 - depth))
    올림수 = math.ceil(num / (10** (길이 - depth))) * (10 **(길이 - depth))
    

    # print("hohoh",depth, 버림수, 올림수, 합)
    
    recursion(버림수, depth - 1, 합 + int(str(abs(num-버림수))[0]))
    recursion(올림수, depth - 1, 합 + int(str(abs(num-올림수))[0]))

    # print(버림수)
    # print(올림수)
    
def solution(storey):

    answer = 0
    global result
    result = int(1e9)
    
    recursion(storey, len(str(storey)), 0)
    
    return result