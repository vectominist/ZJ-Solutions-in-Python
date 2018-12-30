import sys

for s in sys.stdin:
	n = s.split()
	print(int(n[0]) + int(n[1]))
