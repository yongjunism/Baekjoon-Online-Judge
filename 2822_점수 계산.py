import sys
input = sys.stdin.readline

score = [int(input()) for _ in range(8)]
top5 = sorted(score, reverse=True)[:5]
res = [score.index(i) + 1 for i in top5]
print(sum(top5))
print(*sorted(res))