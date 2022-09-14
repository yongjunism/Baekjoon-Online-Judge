import sys
input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')