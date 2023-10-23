import sys
input = sys.stdin.readline

N = int(input())


#상근이가 가지고 있는 카드
card = list(map(int, input().split()))

#정렬
card.sort()

M = int(input())

query = list(map(int, input().split()))


for num in query:

    s = 0
    e = len(card) - 1
    mid = 0
    while s + 1 < e:
        mid = (s+e)//2
        if card[mid] < num:
            s = mid
        else:
            e = mid
    if num in [card[s],card[e]]:
        print(1)
    else:
        print(0)