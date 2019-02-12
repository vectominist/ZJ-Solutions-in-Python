import sys

s = sys.stdin.readline()
num = s.split()
n = int(num[0])

ans = 0
s = sys.stdin.readline()
num = s.split()

for i in range(n):
    ans += (i + 1) * (int(num[i]))

print(ans)
