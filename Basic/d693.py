import sys

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n == 0:
        break
    s = sys.stdin.readline()
    num = s.split()
    
    now = int(num[0])
    for i in range(1, n):
        a = int(num[i])
        if now > a:
            now = now * a // GCD(now, a)
        else:
            now = now * a // GCD(a, now)
    print(now)

