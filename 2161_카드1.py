from collections import deque

n = int(input())
card = deque(range(1, n+1))

while card:
    print(card.popleft())
    card.rotate(-1)