import sys
input = sys.stdin.readline

n = int(input())

log = {}
for _ in range(n):
    name, msg = input().rstrip().split()

    if msg == 'enter':
        log[name] = 1
    else:
        del log[name]

for i in sorted(log, reverse=True):
    print(i)