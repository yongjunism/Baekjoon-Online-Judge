# 이분 탐색 풀이
import sys
input = sys.stdin.readline

def binary_search(arr, target):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0

n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    print(binary_search(arr1, i))

# set() 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr1 = set(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr1:
        print(1)
    else:
        print(0)