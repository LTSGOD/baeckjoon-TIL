N = int(input())

result = [0,0,2]

for i in range(3, N + 1):
    if i % 2 == 0:
        result.append(i*i // 2)
    else:
        result.append(result[i-1] + 2 * (i//2) + 1)
print(result[N])