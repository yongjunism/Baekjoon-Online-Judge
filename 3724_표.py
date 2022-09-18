import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = []

    for j in range(m):
        mul = 1
        for i in range(n):
            mul *= arr[i][j]
        res.append([j+1, mul])

    res.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(res[0][0])