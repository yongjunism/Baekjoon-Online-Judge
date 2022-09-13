import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

AB = [[0]*K for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            AB[n][k] += A[n][m] * B[m][k]
    print(' '.join(map(str, AB[n])))