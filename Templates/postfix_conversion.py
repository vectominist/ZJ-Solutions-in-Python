import sys

for s in sys.stdin:
	num = s.split()

	op = []
	postfix = []
	# build postfix list
	for i in num:
		if i == '(':
			op.append(i)
		elif i == ')':
			while len(op) > 0:
				if op[-1] == '(':
					op.pop()
					break
				else:
					postfix.append(op[-1])
					op.pop()

		elif (i == '*') or (i == '/') or (i == '%'):
			while len(op) > 0:
				if (op[-1] == '(') or (op[-1] == '+') or (op[-1] == '-'):
					break
				else:
					postfix.append(op[-1])
					op.pop()
			
			op.append(i)
		elif (i == '+') or (i == '-'):
			while len(op) > 0:
				if op[-1] == '(':
					break
				else:
					postfix.append(op[-1])
					op.pop()
			
			op.append(i)
		else:
			postfix.append(i)
	
	while len(op) > 0:
		if op[-1] == '(':
			op.pop()
			break
		else:
			postfix.append(op[-1])
			op.pop()
	
	'''
	postStr = ''
	for i in postfix:
		postStr += i + ' '
	
	print(postStr)
	'''

	ans = []
	for i in postfix:
		tmp = 0
		if (i == '+'):
			tmp = ans[-2] + ans[-1]
		if (i == '-'):
			tmp = ans[-2] - ans[-1]
		if (i == '*'):
			tmp = ans[-2] * ans[-1]
		if (i == '/'):
			tmp = ans[-2] // ans[-1]
		if (i == '%'):
			tmp = ans[-2] % ans[-1]
		if (i == '+') or (i == '-') or (i == '*') or (i == '/') or (i == '%'):
			ans.pop()
			ans.pop()
			ans.append(tmp)
		else:
			ans.append(int(i))
		# print(ans)
		
	print(ans[0])

