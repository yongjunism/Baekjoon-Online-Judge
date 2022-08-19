self_num = set(range(1, 10001))
not_self = set()

def d(n):
    d_n = n
    for i in str(n):
        d_n += int(i)
    return d_n

for n in range(1, 10001):
    d_n = d(n)
    if d_n < 10001:
        not_self.add(d_n)

self_num = self_num - not_self

for i in sorted(self_num):
    print(i)