import sys
input = sys.stdin.readline

n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if box[0] > crane[0]:
    print(-1)
    exit()

time = 0
while box:
    for i in range(len(crane)):
        for j in range(len(box)):
            if crane[i] >= box[j]:
                del box[j]
                break
    time += 1
print(time)