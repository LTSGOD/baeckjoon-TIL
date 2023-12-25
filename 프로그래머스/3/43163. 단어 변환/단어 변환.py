
def check(a, b):
    
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    
    #한글자만 다른경우
    if count == (len(a) - 1):
        return True
    else:
        return False
        
def recursion(begin, words, target):
    global answer
    if begin == target:
        return True
    
    for i,w in enumerate(words):
        if visited[i]:
            continue
        if check(begin, w):
            visited[i] = True
            answer += 1
            if recursion(w, words, target):
                print(w)
                return True
            else:
                visited[i] = False
            answer -= 1

    return False
def solution(begin, target, words):
    global visited
    global answer
    visited = [False for _ in words]
    answer = 0
    if recursion(begin, words, target):
        return answer
    else:
        return 0
  