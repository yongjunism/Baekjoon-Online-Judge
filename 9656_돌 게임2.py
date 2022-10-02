n = int(input())

dp = ['' for _ in range(1001)]
dp[1] = 'CY'

for i in range(1, 1000):
    if dp[i] == 'CY':
        if dp[i+1] == '':
            dp[i+1] = 'SK'
        if i + 3 < 1000:
            dp[i+3] = 'SK'
    elif dp[i] == 'SK':
        if dp[i+1] == '':
            dp[i+1] = 'CY'
        if i + 3 < 1000:
            dp[i+3] = 'CY'
    if dp[n]:
        print(dp[n])
        break