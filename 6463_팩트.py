while True:
    fact = 1
    i = 0
    try:
        n = int(input())
        while i != n:
            i += 1
            fact *= i
        while fact % 10 == 0:
            fact //= 10
        print(f'{n:5} -> {fact % 10}')
    except:
        break