import sys
import math
input = sys.stdin.readline

N, r, c = map(int, input().split())

tmp = N

start = 0
end = (2**(2*N))-1
while True:
    quater = 2**(2*tmp-2)
    # print(quater)
    # print(tmp)
    # print(r, c)
    # print(start, end)
    # print("-------------------")

    if(r < 2**(tmp-1) and c < 2**(tmp-1)):
        # print("1")
        if(tmp == 1):
            print(start)
            break
        end = start+quater - 1
    elif(r < 2**(tmp-1) and c >= 2**(tmp-1)):
        # print("2")
        if(tmp == 1):
            print(start+1)
            break
        start += quater
        end = start + quater-1
        c = c - math.sqrt(quater)
    elif(r >= 2**(tmp-1) and c < 2**(tmp-1)):
        # print("3")
        if(tmp == 1):
            print(start+2)
            break
        start += 2*quater
        end = start+quater-1
        r = r - int(math.sqrt(quater))
    else:
        if(tmp == 1):
            print(start+3)
            break
        # print("4")
        start += 3*quater
        end = start+quater-1
        r = r - int(math.sqrt(quater))
        c = c - int(math.sqrt(quater))

    tmp -= 1
