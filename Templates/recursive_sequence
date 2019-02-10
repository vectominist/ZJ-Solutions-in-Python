import sys

s = sys.stdin.readline()
num = s.split()

x1 = int(num[0])
x2 = int(num[1])
a  = int(num[2])
b  = int(num[3])
n  = int(num[4])
n -= 2

base = []
base.append([b     , a])
base.append([int(1), int(0)])

matrix = []
matrix.append([int(1), int(0)])
matrix.append([int(0), int(1)])

tmp = []
tmp.append([int(1), int(0)])
tmp.append([int(0), int(1)])

MOD = int(1000000007)

while n > 0:
	if n & 1:
		tmp[0][0] = (base[0][0] * matrix[0][0] + base[0][1] * matrix[1][0]) % MOD
		tmp[0][1] = (base[0][0] * matrix[0][1] + base[0][1] * matrix[1][1]) % MOD
		tmp[1][0] = (base[1][0] * matrix[0][0] + base[1][1] * matrix[1][0]) % MOD
		tmp[1][1] = (base[1][0] * matrix[0][1] + base[1][1] * matrix[1][1]) % MOD

		matrix[0][0] = tmp[0][0]
		matrix[0][1] = tmp[0][1]
		matrix[1][0] = tmp[1][0]
		matrix[1][1] = tmp[1][1]

	tmp[0][0] = (base[0][0] * base[0][0] + base[0][1] * base[1][0]) % MOD
	tmp[0][1] = (base[0][0] * base[0][1] + base[0][1] * base[1][1]) % MOD
	tmp[1][0] = (base[1][0] * base[0][0] + base[1][1] * base[1][0]) % MOD
	tmp[1][1] = (base[1][0] * base[0][1] + base[1][1] * base[1][1]) % MOD

	base[0][0] = tmp[0][0]
	base[0][1] = tmp[0][1]
	base[1][0] = tmp[1][0]
	base[1][1] = tmp[1][1]

	n = n >> 1

# print(matrix)
xn = (matrix[0][0] * x2 + matrix[0][1] * x1) % MOD

print(xn)
