import sys

s = sys.stdin.readline()
num = s.split()
N = int(s)

for i in range(N):
	s = sys.stdin.readline()
	num = s.split()
	a = int(num[0])
	b = int(num[1])
	c = int(num[2])
	d = int(num[3])

	if (a - b) == (b - c) and (b - c) == (c - d):
		print("%d %d %d %d %d" % (a, b, c, d, d + (d - c)))
	else:
		print("%d %d %d %d %d" % (a, b, c, d, d * d / c))
