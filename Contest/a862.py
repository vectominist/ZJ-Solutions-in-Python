import sys

for s in sys.stdin:
    num = s.split()
    V = float(num[0])
    R = float(num[1])
    V *= 1000.0
    print('%.4lf' % (V / R))

