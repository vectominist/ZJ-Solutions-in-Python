import sys

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    s = sys.stdin.readline()
    num = s.split()
    ls = []
    for i in num:
        ls.append(int(i))
    ls.sort()
    ans1 = ''
    ans2 = -1
    ans3 = -1
    for i in ls:
        if ans1 == '':
            ans1 = str(i)
        else:
            ans1 += ' ' + str(i)
        if i < 60:
            ans2 = i
        if i >= 60 and ans3 == -1:
            ans3 = i
    
    print(ans1)
    if ans2 < 0:
        print('best case')
    else:
        print(ans2)
    
    if ans3 < 0:
        print('worst case')
    else:
        print(ans3)
