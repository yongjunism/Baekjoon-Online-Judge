start, end = map(int, input().split())
n = int(input())
shortcut = [abs(int(input()) - end) for _ in range(n)]
print(min(abs(start-end), min(shortcut)+1))