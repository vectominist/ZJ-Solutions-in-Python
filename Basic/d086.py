import sys

for s in sys.stdin:
    num = s.split()
    st = num[0]
    if st == '0':
        break
    
    ans = 0
    for i in st:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            ans += ord(i) - ord('a') + 1
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            ans += ord(i) - ord('A') + 1
        else:
            ans = -1
            break
    if ans == -1:
        print('Fail')
    else:
        print(ans)
