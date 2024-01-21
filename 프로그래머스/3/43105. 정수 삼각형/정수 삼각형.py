def solution(triangle):
    
    for i, line in enumerate(triangle):
        if i == 0:
            continue
        for j, current in enumerate(line):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(line) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    return max(triangle[-1])