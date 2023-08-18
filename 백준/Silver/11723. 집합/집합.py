import sys

input = sys.stdin.readline

M = int(input())

result = set()

for _ in range(M):
    command = input().rstrip().split()
    
    if command[0] == "add":
        result.add(int(command[1]))
    elif command[0] =="check":
        if int(command[1]) in result:
            print("1")
        else:
            print("0")
    elif command[0] == "remove":
        if int(command[1]) in result:
            result.discard(int(command[1]))
    elif command[0] == "toggle":
        if int(command[1]) in result:
            result.discard(int(command[1]))
        else:
            result.add(int(command[1]))
    elif command[0] == "all":
        result = set([i for i in range(1,21)])
    elif command[0] == "empty":
        result = set()