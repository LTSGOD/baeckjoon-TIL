def solution(msg):
    answer = []
    사전 = {chr(64 + i):i for i in range(1, 27)}
    # print(사전)
    last_num = 27
    i = 0

    while i < len(msg):
        if i == len(msg) - 1:
            answer.append(사전[msg[i]])
            break
        j = i + 1
        tmp = msg[i]
        count = 1
        while j < len(msg):
            tmp += msg[j]
            if 사전.get(tmp):
                pass
            else:
                사전[tmp] = last_num
                last_num += 1
                # print(tmp)
                answer.append(사전[tmp[:-1]])
                i += count
                break
            j += 1
            count += 1
        else:
            answer.append(사전[tmp])
            break
        
    return answer