N = int(input())

room = []

for i in range(N):
    seat = list(map(str, input().split()))
    room.append(seat)
    
def check(room):
    row, col = 0, 0
    for i in range(N):
        for j in range(N-1):
            if room[i][j] == '.' and room[i][j+1] == '.':
                row += 1
                break
    
    for j in range(N):
        for i in range(N-1):
            if room[i][j] == '.' and room[i+1][j] == '.':
                col += 1
                break
    print(row, col)

check(room)