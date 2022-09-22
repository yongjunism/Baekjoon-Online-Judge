def binary_search(n):
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid**2 == n:
            return mid
        elif mid**2 > n:
            high = mid -1
        else:
            low = mid + 1
    return -1

n = int(input())
print(binary_search(n))
