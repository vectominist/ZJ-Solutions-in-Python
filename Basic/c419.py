import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    for i in range(n):
        print('_' * (n - i - 1) + '*' * (i + 1))
