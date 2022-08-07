import sys
input = sys.stdin.readline

def binary_search(trees, m):
    low, high = 0, max(trees)
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid
        if total >= m:
            low = mid + 1
        else:
            high = mid -1
    return high

n, m = map(int,input().split())
trees = list(map(int, input().split()))
print(binary_search(trees, m))