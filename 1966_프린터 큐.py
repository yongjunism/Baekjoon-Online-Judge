import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    idx = list(range(n))
    target = idx[m]
    cnt = 0

    while priority:
        if priority[0] == max(priority):
            cnt += 1
            if idx[0] == target:
                print(cnt)
                break
            priority.pop(0)
            idx.pop(0)
        else:
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))