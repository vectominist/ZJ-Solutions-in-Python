import sys

Rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

IntM = ['', 'M', 'MM', 'MMM']
IntC = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
IntX = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
IntI = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

def RomeToInt(s):
	if s == '':
		return int(0)
	# s : string
	x = int(0)
	l = len(s)
	i = 0
	while i < l:
		if (i + 1 < l) and (Rome[s[i + 1:i + 2]] > Rome[s[i:i + 1]]):
			x += Rome[s[i + 1:i + 2]] - Rome[s[i:i + 1]]
			i += 1
		else:
			x += Rome[s[i:i + 1]]
		i += 1
	
	return x

def IntToRome(x):
	if x == 0:
		return 'ZERO'

	return IntM[x // 1000] + IntC[(x % 1000) // 100] + IntX[(x % 100) // 10] + IntI[x % 10]


for s in sys.stdin:
	num = s.split()
	if num[0] == '#':
		break
	ans = RomeToInt(num[0]) - RomeToInt(num[1])
	if ans < 0:
		ans = -ans
	print(IntToRome(ans))
