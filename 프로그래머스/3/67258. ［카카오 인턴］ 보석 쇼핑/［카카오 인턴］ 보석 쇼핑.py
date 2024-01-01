def solution(gems):
    answer = [0, int(1e9)]
    종류 = set(gems)
    # print(종류)
    보석사전 = {gems[0] : 1}
    left = 0
    right = 0
    while (left < len(gems) and right < len(gems)):
        
        # 종류가 다 들어있으면
#         print("--------------------")
#         print("left ", left, "right ", right)
#         print("보석사전:", 보석사전)
#         print(answer)
        
        
        if len(보석사전) == len(종류):
            
            #현재 정답보다 더 작다면
            if len(보석사전) == len(종류):
                if (answer[1] - answer[0]) > right - left:
                    answer = [left + 1, right + 1]
            #보석사전에서 빼기
            if 보석사전[gems[left]] == 1:
                del 보석사전[gems[left]]
            else:
                보석사전[gems[left]] -= 1
                
            left += 1
        else:
            right += 1
            
            if right == len(gems):
                break
            #보석추가
            if 보석사전.get(gems[right]):
                보석사전[gems[right]] += 1
            else:
                보석사전[gems[right]] = 1
    return answer