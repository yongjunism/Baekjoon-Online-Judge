import sys
input = sys.stdin.readline

n = int(input())
word = [input().rstrip() for _ in range(n)]

word = list(set(word))
word.sort(key=lambda x: (len(x), x))

print('\n'.join(word))