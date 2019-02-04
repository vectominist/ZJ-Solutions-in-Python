import sys

def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, a % b)

for s in sys.stdin:
	num = s.split()
	if len(num) == 0:
		continue
	a = int(num[0])
	b = int(num[1])
	if a < b:
		tmp = a
		a = b
		b = tmp
	print(GCD(a, b))

