import sys

for s in sys.stdin:
    num = s.split()
    a = int(num[0])
    b = int(num[2])
    if num[1] == '+':
        print(a + b)
    elif num[1] == '-':
        print(a - b)
    elif num[1] == '*':
        print(a * b)
    elif num[1] == '/':
        print(a // b)
