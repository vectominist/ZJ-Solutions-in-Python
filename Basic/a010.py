import sys
# import numpy as np


# Prime Sieve
MAX_N = int(1000005)
#p = np.ones(1000005, dtype = bool)
p = [True] * 1000001
p[0] = False
p[1] = False

primeNum = int(0)
#primes = np.zeros(78498, dtype = int)
primes = [int(0)] * 78498

for i in range(1000):
	if p[i] == False:
		continue
	else:
		# i is prime !
		primes[primeNum] = i
		primeNum += 1
		j = i ** 2
		while j < 1000000:
			p[j] = False
			j += i

for i in range(1001, 1000000):
	if p[i] == True:
		primes[primeNum] = i
		primeNum += 1


for s in sys.stdin:
	n = int(s)
	res = ''
	for i in primes:
		if n == 0:
			break
		if n % i == 0:
			cnt = 0
			while (n % i == 0) and (n > 0):
				cnt += 1
				n /= i
			
			if res == '':
				res += str(i)
				if cnt > 1:
					res += '^' + str(cnt)
			else:
				res += ' * ' + str(i)
				if cnt > 1:
					res += '^' + str(cnt)
	print(res)
