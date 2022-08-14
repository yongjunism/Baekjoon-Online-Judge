import sys
input = sys.stdin.readline

n = int(input())
data = [list(input().rstrip().split()) for _ in range(n)]

data.sort(key = lambda x: int(x[0]))
for age, name in data:
    print(age, name)