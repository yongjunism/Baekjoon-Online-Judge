import sys
input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    cnt = 0
    for num in range(n, m+1):
        if len(str(num)) == len(set(str(num))):
            cnt += 1
    print(cnt)