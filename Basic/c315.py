import sys

s = sys.stdin.readline()
num = s.split()
N = int(num[0])

x = 0
y = 0
dx = [  0,  1,  0, -1]
dy = [  1,  0, -1,  0]

for i in range(N):
    s = sys.stdin.readline()
    num = s.split()
    a = int(num[0])
    b = int(num[1])
    x += dx[a] * b
    y += dy[a] * b

print('%d %d' % (x, y))
