import sys

for s in sys.stdin:
	n = s.split()
	year = int(n[0])

	if year % 400 == 0:
		print("閏年")
	elif year % 100 == 0:
		print("平年")
	elif year % 4 == 0:
		print("閏年")
	else:
		print("平年")
