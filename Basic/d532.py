import sys

s = sys.stdin.readline()
num = s.split()
a = int(num[0])
b = int(num[1])

ans = 0
for i in range(a, b + 1):
    if i % 400 == 0:
        ans += 1
    elif i % 100 == 0:
        pass
    elif i % 4 == 0:
        ans += 1

print(ans)
