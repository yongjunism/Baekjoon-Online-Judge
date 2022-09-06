n = int(input())
series = [int(input()) for _ in range(n)]
stack, op = [], []
cnt = 1

for num in series:
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')

if not stack:
    print('\n'.join(op))
else:
    print('NO')