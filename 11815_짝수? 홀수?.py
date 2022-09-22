import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

for i in x:
    if i == int(i ** 0.5) ** 2:
        print(1, end=' ')
    else:
        print(0, end=' ')