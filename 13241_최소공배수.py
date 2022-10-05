def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
print(a * b // gcd(a, b))