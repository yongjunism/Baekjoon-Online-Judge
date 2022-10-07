import sys
input = sys.stdin.readline

def available(channel):
    for s in str(channel):
        if s in broken:
            return False
    return True

n = int(input())
m = int(input())

if m:
    broken = input().split()
else:
    broken = []
cnt = abs(100 - n)

for i in range(1000001):
    if available(i):
        cnt = min(cnt, len(str(i)) + abs(i - n))
print(cnt)