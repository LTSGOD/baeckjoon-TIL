import sys

input = sys.stdin.readline

M = int(input())

result = set()

tmp = set([str(i) for i in range(1, 21)])
for _ in range(M):
    command = list(input().split())

    if(command[0] == "add"):
        result.add(command[1])
    elif(command[0] == "remove"):
        if(command[1] in result):
            result.remove(command[1])
    elif(command[0] == "check"):
        if(command[1] in result):
            print(1)
        else:
            print(0)
    elif(command[0] == "toggle"):
        if(command[1] in result):
            result.remove(command[1])
        else:
            result.add(command[1])
    elif(command[0] == "all"):
        result = tmp
    else:
        result = set()
