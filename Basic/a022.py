import sys

for s in sys.stdin:
	st = s.split()
	s = st[0]
	l = len(s)
	hl = l // 2
	i = int(0)
	ans = True
	# print('%d %d' % (l, hl))
	while i <= hl:
		# print('%d -> %c %c' % (i, s[i], s[l - i - 1]))
		if s[i] != s[l - i - 1]:
			ans = False
			break
		i += 1
	
	if ans == True:
		print('yes')
	else:
		print('no')
	
