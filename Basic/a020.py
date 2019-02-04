import sys

codeDict = { 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, \
	'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, \
	'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33 }

for s in sys.stdin:
	ans = int(0)
	cd = codeDict[s[0]]
	ans += (cd % 10) * 9 + (cd // 10)
	i = 1
	while i < 9:
		ans += int(s[i: i + 1]) * (9 - i)
		i += 1
	ans += int(s[9: 10])
	#print(ans)
	if ans % 10 == 0:
		print('real')
	else:
		print('fake')
	
