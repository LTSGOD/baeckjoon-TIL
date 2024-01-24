#밴 된 아이디가 유저네임 추정되면 True, 아니면 False
def check(user_name, banned_name):
    
    user_len = len(user_name)
    banned_len = len(banned_name)
    
    #길이가다르면 
    if user_len != banned_len:
        return False

    i = 0
    while i < user_len:
        
        #*이면 continue
        if banned_name[i] == "*":
            i += 1
            continue
            
        #글자가 다르면 바로 False
        if user_name[i] != banned_name[i]:
            return False
        
        i += 1
    
    return True

def recursion(depth,user_id, banned_id):
    global answer
    
    if depth == len(banned_id):
        
        사전.add(tuple(sorted(result)))
        
        return
    
    for i, b_id in enumerate(banned_id):
        
        if banned_visited[i]:
            continue
    
        banned_visited[i] = True
        
        for j, u_id in enumerate(user_id):
            
            if user_visited[j]:
                continue
            if check(u_id, b_id):
                user_visited[j] = True
                result.append(u_id)
                
                recursion(depth+1, user_id, banned_id)
                
                result.pop()
                user_visited[j] = False
        banned_visited[i] = False
#       return 추가해서 테스트 케이스 5번 통과
        return

def solution(user_id, banned_id):
    global answer
    global result
    global 사전
    사전 = set()

    # print(사전)
    result = []
    answer = 0
    
    global user_visited
    global banned_visited
    user_visited = [False for _ in range(len(user_id))]
    banned_visited = [False for _ in range(len(banned_id))]
    
    recursion(0, user_id, banned_id)
    print(사전)
    return len(사전)

