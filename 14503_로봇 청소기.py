import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cleaned = 1
space[r][c] = 2

def next_dir(dir):
    if dir == 0:
        return [3, 2, 1, 0]
    elif dir == 1:
        return [0, 3, 2, 1]
    elif dir == 2:
        return [1, 0, 3, 2]
    else:
        return [2, 1, 0, 3]

while True:
    dirs = next_dir(d)
    checked = False
    for dir in dirs:
        nx = r + dx[dir]
        ny = c + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and space[nx][ny] == 0:
            r, c = nx, ny
            space[nx][ny] = 2
            cleaned += 1
            d = dir
            checked = True
    if checked == False:
        r -= dx[dir]
        c -= dy[dir]
        if space[r][c] == 1:
            break
print(cleaned)