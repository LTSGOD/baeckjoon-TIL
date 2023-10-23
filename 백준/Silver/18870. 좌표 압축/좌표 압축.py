import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
num_set = sorted(list(set(num_list)))


num_dict = {value: index for index, value in enumerate(num_set)}

for num in num_list:
    print(num_dict[num], end=" ")