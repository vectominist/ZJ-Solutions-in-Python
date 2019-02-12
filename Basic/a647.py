import sys

def ABS(x):
    if x > 0:
        return x
    else:
        return -x

EPS = 1e-8

s = sys.stdin.readline()
num = s.split()
n = int(num[0])

for i in range(n):
    s = sys.stdin.readline()
    num = s.split()
    m = float(num[0])
    p = float(num[1])

    x = (p - m) / m
    if x > 0:
        x += EPS
    else:
        x -= EPS
    
    if (x > 0.1 - EPS) or (x < -0.07 + EPS):
        print('%.2lf%% dispose' % (x * 100))
    else:
        if ABS(x) < 0.0001:
            x = EPS
        
        print('%.2lf%% keep' % (x * 100))
