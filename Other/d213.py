import sys

a = [0] * 63
b = [0] * 63

b[0] = 2
a[0] = 2

for i in range(1, 10):
    b[i] = b[i - 1] << 1
    a[i] = a[i - 1] + b[i]

for i in range(10, 63):
    b[i] = b[i - 1] << 1
    a[i] = a[i - 1] + b[i] - b[i - 10]

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    print('{0}'.format(a[n]))
