import sys

def MAX(x, y):
	if x > y:
		return x
	else:
		return y

initH = (0, 0)

for s in sys.stdin:
	num = s.split()
	N = int(num[0])
	
	stack = [initH]
	ans = int(0)

	for i in range(N):
		s = sys.stdin.readline()
		num = s.split()
		x = int(num[0])

		while len(stack) > 1:
			if stack[-1][0] > x:
				ans = MAX(ans, stack[-1][0] * (i - stack[-2][1]))
				stack.pop()
			elif stack[-1][0] == x:
				ans = MAX(ans, stack[-1][0] * (i + 1 - stack[-2][1]))
				stack.pop()
			else:
				break
		stack.append((x, i + 1))
	
	i = int(0)
	for i in range(len(stack)):
		if i == 0:
			continue
		ans = MAX(ans, stack[i][0] * (N - stack[i - 1][1]))
	print(ans)

