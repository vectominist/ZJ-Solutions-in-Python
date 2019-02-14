import sys

for s in sys.stdin:
    num = s.split()
    h = int(num[0])
    w = int(num[1])
    print(2 * (h + w))

