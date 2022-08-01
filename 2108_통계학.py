import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

num.sort()
print(int(round(sum(num)/n, 0)))
print(num[n//2])

temp = Counter(num).most_common()
if len(temp) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])
print(num[-1] - num[0])