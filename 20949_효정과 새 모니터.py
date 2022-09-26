n = int(input())
ppi = []

for i in range(n):
    w, h = map(int, input().split())
    ppi.append([w**2+h**2, i+1])
    
for i in sorted(ppi, key=lambda x: (x[0], -x[1]), reverse=True):
    print(i[1])