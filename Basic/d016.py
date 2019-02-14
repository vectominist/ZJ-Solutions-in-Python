import sys

for s in sys.stdin:
    num = s.split()
    stack = []
    for i in num:
        # print(stack)
        if ord(i[0]) >= ord('0') and ord(i[0]) <= ord('9'):
            stack.append(int(i))
        elif i == '+':
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            stack.append(b + a)
        elif i == '-':
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            stack.append(b - a)
        elif i == '*':
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            stack.append(b * a)
        elif i == '/':
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            stack.append(b // a)
        elif i == '%':
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            stack.append(b % a)
    
    print(stack[0])

