def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def solution(w,h):
    if w > h:
        tmp = w
        w = h
        h = tmp
    
    최대공약수 = gcd(h,w)
    result = h * w
    if 최대공약수 != 1:
        h = (h // 최대공약수)
        w = (w // 최대공약수)
    
    # answer = result - 최대공약수 *(2 * w)
    answer = result - 최대공약수 * (h + w - 1)
    return answer