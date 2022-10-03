n = int(input())

for _ in range(n):
    s, p = input().rstrip().split()
    cnt = s.count(p)
    print(cnt + len(s.replace(p, '')))