import sys

def fastPow(x, n):
	# calculating x ^ n
	ans = 1
	while n > 0:
		if (n & 1):
			ans *= x
		x = x ** 2
		n = n >> 1
	return ans


for s in sys.stdin:
	#s = sys.stdin.readline()
	num = s.split()
	n = int(num[0])
	m = int(num[1])
	if (n == 0) and (m == 0):
		break
	print(fastPow(n, m))
