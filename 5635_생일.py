import sys
input = sys.stdin.readline

n = int(input())
birth = [list(map(str, input().split())) for _ in range(n)]

birth.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(birth[-1][0])
print(birth[0][0])