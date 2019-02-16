import sys

for s in sys.stdin:
    num = s.split()
    d = int(num[0])
    a = [1]
    b = [1]
    ans = 1
    for i in range(1, 50):
        a.append(a[-1] + b[-1])
        b.append(b[-1] + d)
        ans += a[-1]
    print(ans)
