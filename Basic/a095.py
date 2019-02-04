import sys

for s in sys.stdin:
	num = s.split()
	N = int(num[0])
	M = int(num[1])
	if N > M:
		print(M + 1)
	else:
		print(M)

