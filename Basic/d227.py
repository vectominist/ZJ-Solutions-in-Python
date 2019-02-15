import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n & 1:
        print(n - 1)
    else:
        print(n)
