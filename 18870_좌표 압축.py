import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_sort = sorted(list(set(arr)))
dic = {arr_sort[i]: i for i in range(len(arr_sort))}

for coord in arr:
    print(dic[coord], end=' ')