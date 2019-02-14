import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    S = 0
    for i in range(1, n):
        if n % i == 0:
            S += i
    if S > n:
        print('盈數')
    elif S == n:
        print('完全數')
    else:
        print('虧數')
