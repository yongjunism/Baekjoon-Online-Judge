for i in range(int(input())):
    arr = list(map(int, input().split()))
    n, score = arr[0], sorted(arr[1:])
    MIN, MAX = score[0], score[-1]
    gap = max(score[i+1] - score[i] for i in range(n-1))
    print('Class', i+1)
    print(f'Max {MAX}, Min {MIN}, Largest gap {gap}')