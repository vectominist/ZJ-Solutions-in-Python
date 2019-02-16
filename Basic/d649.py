import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n == 0:
        break
    for i in range(1, n + 1):
        print('_' * (n - i) + '+' * i)
    print('')

