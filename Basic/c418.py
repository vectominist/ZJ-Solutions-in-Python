import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    for i in range(n):
        print('*' * (i + 1))
