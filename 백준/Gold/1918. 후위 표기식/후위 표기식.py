import sys
input = sys.stdin.readline


중위표기식 = input().rstrip()

answer = ''
부호 = []

for s in 중위표기식:

    if s not in ['+', '-', '/', '*','(',')']:
        answer+=s
    else:
        if s == ')':
            tmp = 0 
            while 부호 and 부호[-1]!='(':
                answer+= 부호.pop()
            부호.pop()
        elif s == '(':
          부호.append(s)
        elif s == '+' or s == '-':
            while 부호 and 부호[-1] != '(':
                answer+= 부호.pop()
            부호.append(s)
        else:
            while 부호 and (부호[-1] == '*' or 부호[-1]=='/'):
                answer+= 부호.pop()
            부호.append(s)
        
while 부호:
    answer+=부호.pop()

print(answer)