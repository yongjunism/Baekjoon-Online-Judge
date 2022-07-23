import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
res = sys.maxsize

for x in range(n-7):
    for y in range(m-7):
        w_cnt, b_cnt = 0, 0

        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i + j) % 2 == 0 :
                    if board[i][j] != 'W': w_cnt += 1
                    if board[i][j] != 'B': b_cnt += 1
                else:
                    if board[i][j] != 'B': w_cnt += 1
                    if board[i][j] != 'W': b_cnt += 1
        res = min(res, w_cnt, b_cnt)

print(res)