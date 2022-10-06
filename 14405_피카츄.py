s = input().rstrip()

word = ['pi', 'ka', 'chu']
for i in word:
    s = s.replace(i, ' ')

if len(s.strip()) == 0:
    print('YES')
else:
    print('NO')