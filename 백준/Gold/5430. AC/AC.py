import sys
from collections import deque

input = sys.stdin.readline



n = int(input())

for _ in range(n):

    command = input()
    length = int(input())
    array = input()

    if(len(array) == 3):
        array = deque()
    else:
        array = deque( array[1:-2].split(","))

    front = True
    error = False
    for com in command:
        if com == 'R':
            front = not front
        elif com == 'D':
            if not array:
                error = True
                print("error")
                break
            if front == True:
                array.popleft()
            else:
                array.pop()
    if error:
        continue
    if front == False:
        array.reverse()
    print(f'[{",".join(array)}]')