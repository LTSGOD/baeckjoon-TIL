import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

def dfs(result,start):
    stack = []
    stack.append(start)

    possible = [0] * N
    flag = False
    while(stack):
        current = stack.pop()

        visited[current] = True

        for index, node in enumerate(board[current]):
            if node == 1:
                if index == start:
                    flag = True
                if visited[index] == False:         
                    stack.append(index)
                    possible[index] = 1

    if flag:
        possible[start] = 1
    result.append(possible)

result = []
for i in range(N):
    visited = [False] * N
    dfs(result, i)

for i in result:
    for j in i:
        print(j,end=" ")
    print()