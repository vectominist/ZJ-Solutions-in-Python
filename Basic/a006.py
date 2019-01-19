import sys
import math

for s in sys.stdin:
	n = s.split()
	a = int(n[0])
	b = int(n[1])
	c = int(n[2])
	D = b * b - 4 * a * c
	
	if D > 0:
		x1 = int((- b + math.sqrt(D)) / (2 * a))
		x2 = int((- b - math.sqrt(D)) / (2 * a))
		print("Two different roots x1=%d , x2=%d" % (x1, x2))
	elif D == 0:
		x = int(- b / (2 * a))
		print("Two same roots x=%d" % x)
	else:
		print("No real root")
