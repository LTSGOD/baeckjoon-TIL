# 브루트 포스?
def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    
    if a % b == 0:
        return b
    return gcd(b, a%b)
        
def solution(arrayA, arrayB):
    
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    
    for i in range(0, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
        gcd_b = gcd(gcd_b, arrayB[i])

    flag_A = True
    for num in arrayB:
        if num % gcd_a == 0:
            flag_A = False
            break
    
    flag_B = True
    for num in arrayA:
        if num % gcd_b == 0:
            flag_B = False
            break

    if flag_A and flag_B:
        answer = max(gcd_a, gcd_b)
    elif flag_A:
        answer = gcd_a
    elif flag_B:
        answer = gcd_b
    else:
        answer = 0
        
    return answer