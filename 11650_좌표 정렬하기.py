import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    coord = list(map(int, input().split()))
    arr.append(coord)

sorted_arr = sorted(arr)
for i in range(n):
    print(sorted_arr[i][0], sorted_arr[i][1])