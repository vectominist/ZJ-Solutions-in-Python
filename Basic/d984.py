import sys

for s in sys.stdin:
    s = s.split()
    ls = []
    ls.append((int(s[0]), 'A'))
    ls.append((int(s[1]), 'B'))
    ls.append((int(s[2]), 'C'))
    
    ls.sort()
    second = ls[1][0] + ls[0][0]
    first = ls[2][0]
    if second > first:
        print(ls[1][1])
    else:
        print(ls[2][1])
