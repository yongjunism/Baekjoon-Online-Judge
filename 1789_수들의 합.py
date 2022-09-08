s = int(input())
n, total = 0, 0

for i in range(1, s+1):
    total += i
    n += 1
    if total > s:
        n -= 1
        break
print(n)