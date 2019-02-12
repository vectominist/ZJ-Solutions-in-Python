import sys

def MAX(x, y):
    if x > y:
        return x
    else:
        return y

s = sys.stdin.readline()
num = s.split()
n = int(num[0])

ans = -100005
mx = -100005
s = sys.stdin.readline()
num = s.split()
for i in num:
    a = int(i)
    ans = MAX(ans, mx - a)
    mx = MAX(mx, a)

print(ans)
