import sys

input = sys.stdin.readline

M = input()

tmp = ""
result = []

for i in M:
    if i.isdigit():
        tmp += i
    elif(i == '+' or i == '-'):
        result.append(tmp)
        result.append(i)
        tmp = ""
    else:
        result.append(tmp)

answer = 0
minus_flag = False
부호 = '+'
for i, thing in enumerate(result):
    if thing.isdigit():
        if(부호 == '+'):
            answer += int(thing)
        else:
            answer -= int(thing)
    else:
        if thing == '-' and minus_flag == False:
            minus_flag = True
            부호 = '-'
        elif thing == '+' and minus_flag == True:
            부호 = '-'
print(answer)
