def factorial(n):
    if(n == 1):
        return 1
    return n* factorial(n-1)

def solution(n, k):
    # 1 2 3 4
    # 1 2 4 3
    # 1 3 2 4
    # 1 3 4 2
    # 1 4 2 3
    # 1 4 3 2
    # 2 1 3 4
    # 2 1 4 3
    # 2 3 1 4
    # 2 3 4 10
    # 8  6  k 2 n 2
    list1 = [i for i in range(1,n + 1)]
    final = []
    
    while(n > 0):
        partNum = factorial(n)//n
        
        tmp = (k-1) // partNum
        
        result = list1[tmp]
        
        print(tmp)
        print(list1)
        final.append(result)
        list1.remove(result)
        k = k % partNum
        print(k)
        n-=1
    
    return final