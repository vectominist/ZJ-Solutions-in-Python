import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n % 3 == 0:
        print('yes')
    else:
        print('no')

