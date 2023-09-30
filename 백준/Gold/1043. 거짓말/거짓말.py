import sys

input = sys.stdin.readline

N,M = map(int, input().split())

know = list(map(int, input().split()))[1:]

visited = [False] * (N + 1)

for p in know:
    visited[p] = True



parties = []

for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])

for person in know:

    for party in parties:
        if person in party:

            # 아는 사람 리스트에 추가
            for p in party:
                if visited[p] == False:
                    know.append(p)
                    visited[p] = True

count = 0
for party in parties:
    flag = True
    for p in party:
        if visited[p]:
            flag = False
            break
    if flag:
        count +=1 

print(count)