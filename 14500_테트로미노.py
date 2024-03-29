import sys
input = sys.stdin.readline

tetrominoes = [
    [(0,0), (0,1), (0,2), (0,3)],   # 하늘 
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (1,1), (1,0)],   # 노랑
    [(0,0), (1,0), (2,0), (2,1)],   # 주황
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(1,0), (0,0), (0,1), (0,2)],                                                           
    [(0,0), (0,1), (1,1), (2,1)],
    [(2,0), (1,0), (0,0), (0,1)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (2,1)],   # 초록
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (0,1), (0,2), (1,1)],   # 보라
    [(0,1), (1,1), (2,1), (1,0)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)]
]

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

MAX = 4
for x in range(n):
    for y in range(m):
        for tetromino in tetrominoes:
            temp = 0
            for dx, dy in tetromino:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    temp += paper[nx][ny]
                else:
                    break
            if temp > MAX:
                MAX = temp
print(MAX)