import heapq

def solution(n, works):
    #정렬해서 다음 숫자 만큼만 빼는게 최선인것같다.
    
    answer = 0
    
    if sum(works) <= n:
        return answer
    works = [-w for w in works]
    heapq.heapify(works)
    
    print(works)
    while n > 0:
        최댓값 = heapq.heappop(works)
        heapq.heappush(works, 최댓값 + 1)
        n -= 1
    
    for w  in works:
        answer += (w * w)

#     works.sort(reverse=True)
    
#     if sum(works) <= n:
#         return answer

#     i = 0
#     while (i < len(works) - 1) and n > 0:
#         차이 = works[i] - works[i + 1]
#         최소 = min(차이, n)
#         works[i] = works[i] - 최소
#         n -= 최소
#         i += 1
    
#     if n > 0:
#         for i in range(len(works)):
#             works[i] -= 1
    
#     for w in works:
#         answer += (w * w)

    return answer