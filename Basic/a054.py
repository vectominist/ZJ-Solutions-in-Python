import sys

codeDict = { 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, \
	'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, \
	'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33 }

ans = [''] * 11
for i in range(26):
	cc = str(chr(ord('A') + i))
	ans[((codeDict[cc] % 10) * 9 + (codeDict[cc] // 10)) % 10] += cc


for s in sys.stdin:
	num = s.split()
	n = int(num[0])

	i = int(0)
	cnt = n % 10
	while n > 0:
		cnt += (n % 10) * i
		n //= 10
		i += 1
	
	# print(cnt)
	print(ans[(10 - (cnt % 10)) % 10])

