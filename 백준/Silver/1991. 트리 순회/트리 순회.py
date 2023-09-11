import sys

input = sys.stdin.readline

N = int(input())

distance = []

for _ in range(N):
    distance.append(list(input().rstrip().split()))

distance.sort()

def in_order_recursion(node):
    
    if node[1] != ".":
        in_order_recursion(distance[ord(node[1])-65])
    print(node[0],end="")
    if node[2] != ".":
        in_order_recursion(distance[ord(node[2])-65])
    
    return 0 

def pre_order_recursion(node):
    
    print(node[0],end="")
    if node[1] != ".":
        pre_order_recursion(distance[ord(node[1])-65])
    if node[2] != ".":
        pre_order_recursion(distance[ord(node[2])-65])
    
    return 0

def post_order_recursion(node):
    
    if node[1] != ".":
        post_order_recursion(distance[ord(node[1])-65])
    if node[2] != ".":
        post_order_recursion(distance[ord(node[2])-65])
    print(node[0],end="")
    
    return 0 

pre_order_recursion(distance[0])
print()
in_order_recursion(distance[0])
print()
post_order_recursion(distance[0])