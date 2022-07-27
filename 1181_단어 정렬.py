import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
words = list(set(words))

words.sort(key=lambda x: (len(x), x))
print('\n'.join(word))