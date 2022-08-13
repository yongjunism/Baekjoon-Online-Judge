import sys
input = sys.stdin.readline

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
team_start = []
diff = []

def dfs(num, last, n):
    global team_start, diff
    if num == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if i in team_start and j in team_start:
                    start += stat[i][j]
                elif i not in team_start and j not in team_start:
                    link += stat[i][j]
        diff.append(abs(start - link))
    else:
        for i in range(last, n):
            team_start.append(i)
            dfs(num+1, i, n)
            team_start.remove(i)
dfs(0, 0, n)
print(min(diff))