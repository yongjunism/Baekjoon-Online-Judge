import sys
input = sys.stdin.readline

n = int(input())
nums = [i for i in sorted([int(input()) for _ in range(n)])]

for num in nums:
    print(num)