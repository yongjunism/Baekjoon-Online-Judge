import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
rank = sorted(score, reverse=True)
for i in score:
    print(rank.index(i) + 1)