import sys
from collections import deque
input = sys.stdin.readline

dir = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

def bfs(start_x, start_y, dest_x, dest_y):
    q = deque()
    q.append((start_x, start_y))
    board[start_x][start_y] = 1

    while q:
        x, y = q.popleft()
        if x == dest_x and y == dest_y:
            print(board[x][y] - 1)
            return
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    bfs(start_x, start_y, dest_x, dest_y)