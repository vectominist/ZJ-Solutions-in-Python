import sys
import math

def ABS(x):
    if x > 0:
        return x
    else:
        return -x

for s in sys.stdin:
    odd_S = 0
    even_S = 0
    num = s.split()
    for i in num:
        index = 0
        R_num = 0
        for j in range(len(i)):
            if i[j] == ':':
                index = int(i[:j])
                fR = float(i[j + 1:])
                if fR > 0:
                    fR += 1e-10
                else:
                    fR -= 1e-10
                R_num = int(fR * 1000000.0000000)
                break
        if index & 1:
            odd_S += R_num
        else:
            even_S += R_num
    ans = odd_S - even_S
    cnt = 6
    ans = ans
    while ans % 10 == 0 and ans != 0 and cnt > 0:
        ans //= 10
        cnt -= 1
    st = str(ans)
    if ans == 0 or cnt == 0:
        print(st)
    else:
        if st[:-cnt] == '':
            st = '0' + '.' + st
        else:
            st = st[:-cnt] + '.' + st[-cnt:]
        print(st)
