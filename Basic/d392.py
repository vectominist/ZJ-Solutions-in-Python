import sys

for s in sys.stdin:
    num = s.split()
    ans = 0
    for i in num:
        ans += int(i)
    print(ans)
