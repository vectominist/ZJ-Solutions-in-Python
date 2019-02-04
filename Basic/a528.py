import sys

for s in sys.stdin:
	num = s.split()
	N = int(num[0])
	arr = [int(0)] * N
	for i in range(N):
		s = sys.stdin.readline()
		num = s.split()
		arr[i] = int(num[0])
	arr.sort()
	for i in arr:
		print(i)
