import sys

for s in sys.stdin:
    num = s.split()
    st = num[0]
    
    ans = st[0]
    mx = 1
    prev = ''
    cnt = 1
    for i in range(len(st)):
        if st[i] == prev:
            cnt += 1
        else:
            if cnt > mx:
                ans = prev
                mx = cnt
            prev = st[i]
            cnt = 1
    if cnt > mx:
        ans = prev
        mx = cnt
    print('%s %d' % (ans, mx))
