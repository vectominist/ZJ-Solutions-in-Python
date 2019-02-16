import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    a = []
    s = sys.stdin.readline()
    num = s.split()
    for i in num:
        a.append(int(i))
    a.sort()
    ans = ''
    for i in range(n):
        if i == 0:
            ans += str(a[i])
        else:
            ans += ' ' + str(a[i])
    print(ans)
