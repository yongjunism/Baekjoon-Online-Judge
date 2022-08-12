# 조건문 분기 
a, b, v = map(int, input().split())

if (v-a) % (a-b) == 0:
    print((v-a)//(a-b)+1)
else:
    print((v-a)//(a-b)+2)

# math.ceil() 이용
import math

a, b, v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))