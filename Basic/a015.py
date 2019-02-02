import sys

for s in sys.stdin:
	#s = sys.stdin.readline()
	num = s.split()
	r = int(num[0])
	c = int(num[1])

	mat = []
	for i in range(r):
		mat.append([0] * c)
	#print(mat)
	# mat = r * c matrix

	for i in range(r):
		s = sys.stdin.readline()
		num = s.split()
		for j in range(c):
			mat[i][j] = int(num[j])
	#print(mat)

	for j in range(c):
		opstr = ''
		for i in range(r):
			if i != 0:
				opstr += ' '
			opstr += str(mat[i][j])
		print(opstr)

