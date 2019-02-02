import sys

for s in sys.stdin:
	tmp = ''
	for i in s:
		tmp += chr(ord(i) - 7)
	print(tmp)
