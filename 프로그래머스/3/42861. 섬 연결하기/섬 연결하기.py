#MST?

#find 함수 연결되어있는지
#최소 길이 선택
def find(node, num):
    
    if node[num] == num:
        return num
    else:
        return find(node, node[num])
        

def solution(n, costs):
    if n == 1:
        return 0
    node = [i for i in range(n)]
    
    costs.sort(key=lambda x : x[2])
    answer = 0
    count = 0
    i = 0
    while i < len(costs):
        if count == n - 1:
            break
        # print(node)
        left_root = find(node, costs[i][0])
        right_root = find(node, costs[i][1])
        
        if left_root != right_root:
            큰노드 = max(left_root, right_root)
            작은노드 = min(left_root, right_root)
            node[큰노드] = 작은노드
            answer+= costs[i][2]
            count += 1
        i += 1
        
    # print(costs)
    # print(node)
    return answer