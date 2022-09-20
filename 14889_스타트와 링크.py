import sys
input = sys.stdin.readline

def dfs(cnt, last, n):
    global team, diff
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if i in team and j in team:
                    start += stat[i][j]
                elif i not in team and j not in team:
                    link += stat[i][j]
        diff.append(abs(start - link))
    else:
        for i in range(last, n):
            if i not in team:
                team.append(i)
                dfs(cnt+1, i, n)
                team.remove(i)
                
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
team, diff = [], []

dfs(0, 0, n)
print(min(diff))
