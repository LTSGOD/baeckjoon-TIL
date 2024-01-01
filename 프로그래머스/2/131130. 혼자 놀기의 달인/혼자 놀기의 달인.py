def recursion(num, 열린상자, cards, depth):
    
    if 열린상자[num]:
        result.append(depth)
        return
    열린상자[num] = True
    return recursion(cards[num] - 1, 열린상자, cards, depth+1)

def solution(cards):
    열린상자 = [False for _ in range(len(cards) + 1)]

    global result
    result = []
    i = 0
    while i < len(cards):
        recursion(i, 열린상자, cards, 0)
        i += 1
    result.sort(reverse=True)
    print(result)
    return result[0] * result[1]