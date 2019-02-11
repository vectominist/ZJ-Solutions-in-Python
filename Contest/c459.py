import sys

s = sys.stdin.readline()
num = s.split()
b = int(num[0])
N = int(num[1])

tmpN = N
ans = 0
digit = 0
while tmpN > 0:
    digit += 1
    tmpN //= 10

tmpN = N
while tmpN > 0:
    ans += (tmpN % 10) ** digit
    tmpN //= 10

ans2 = 0
i = 0

while ans > 0:
    ans2 += (ans % b) * (10 ** i)
    ans //= b
    i += 1

#print(ans2)

if ans2 == N:
    print('YES')
else:
    print('NO')
