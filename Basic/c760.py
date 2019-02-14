import sys

for s in sys.stdin:
    num = s.split()
    for i in num:
        i = chr(ord(i[0]) - ord('a') + ord('A')) + i[1:]
        print(i)
