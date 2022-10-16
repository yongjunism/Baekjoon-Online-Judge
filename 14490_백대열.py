def gcd(a, b):
    while b > 0:
        tmp, a = a, b
        b = tmp % b
    return a

n, m = map(int, input().split(':'))
g = gcd(n, m)
print(f'{n//g}:{m//g}')