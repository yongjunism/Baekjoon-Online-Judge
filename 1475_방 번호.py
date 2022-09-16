room_num = list(map(int, input()))
print(room_num)
freq = [0] * 9

for num in room_num:
    if num in [6, 9]:
        freq[6] += 1
    else:
        freq[num] += 1

freq[6] = (freq[6] // 2) if (freq[6] % 2 == 0) else (freq[6] // 2 + 1)
print(max(freq))
