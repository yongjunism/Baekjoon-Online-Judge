import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for number in numbers:
    if is_prime(number):
        cnt += 1
print(cnt)