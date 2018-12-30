import sys

for s in sys.stdin:
	n = s.split()
	S = (int(n[0]) * 2 + int(n[1])) % 3
	if S == 0:
		print("普通")
	elif S == 1:
		print("吉")
	else:
		print("大吉")
