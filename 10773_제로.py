K = int(input())
number = []

for _ in range(K):
    num = int(input())
    if num == 0:
        number.pop()
    else:
        number.append(num)
print(sum(number))