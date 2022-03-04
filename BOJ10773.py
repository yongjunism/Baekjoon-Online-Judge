k = int(input())

num = []
sum = 0

for _ in range(k):
    num.append(int(input()))
    sum += num[len(num)-1]
    if num[len(num)-1] == 0:
        num.pop()
        sum -= num[len(num)-1]
        num.pop()

print(sum)
