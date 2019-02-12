import sys
import math

'''
def isSqr(x):
    sqrtx = int(math.floor(math.sqrt(x)))
    if sqrtx ** 2 == x:
        return sqrtx
    elif (sqrtx + 1) ** 2 == x:
        return sqrtx + 1
    elif (sqrtx - 1) ** 2 == x:
        return sqrtx - 1
    else:
        return -1

ans = []
MAXK = 1000
for m in range(1, MAXK):
    a1 = isSqr(5 * m * m - 4)
    if a1 > 0:
        n = (m + a1)
        if (n & 1) == 0:
            n >>= 1
            ans.append((n, m))
    a1 = isSqr(5 * m * m + 4)
    if a1 > 0:
        n = (m + a1)
        if (n & 1) == 0:
            n >>= 1
            ans.append((n, m))

for i in ans:
    print(i)
'''

fib_seq = []
fib_seq.append(1)
fib_seq.append(1)
for i in range(2, 45):
    newfib = fib_seq[i - 1] + fib_seq[i - 2]
    fib_seq.append(newfib)


for s in sys.stdin:
    num = s.split()
    k = int(num[0])
    
    for i in range(45):
        if fib_seq[i] > k:
            print('%d %d' % (fib_seq[i - 2], fib_seq[i - 1]))
            break
