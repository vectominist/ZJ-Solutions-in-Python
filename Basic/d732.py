import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    k = int(num[1])

    s = sys.stdin.readline()
    num = s.split()
    a = []
    for i in num:
        a.append(int(i))
    s = sys.stdin.readline()
    num = s.split()
    for i in num:
        x = int(i)
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) >> 1
            if a[m] <= x:
                l = m
            else:
                r = m
        if a[l] == x:
            print(l + 1)
        else:
            print(0)
