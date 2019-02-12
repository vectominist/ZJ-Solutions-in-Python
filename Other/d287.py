import sys

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)

for s in sys.stdin:
    num = s.split()
    a = int(num[0])
    b = int(num[1])

    if a < b:
        tmp = a
        a = b
        b = tmp
    print(a + b - GCD(a, b))
