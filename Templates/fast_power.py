def fastPow(x, n):
	# calculating x ^ n
	ans = 1
	while n > 0:
		if (n & 1):
			ans *= x
		x = x ** 2
		n = n >> 1
	return ans
