import sys

for s in sys.stdin:
    num = s.split()
    
    ans = 0
    for i in num:
        check = True
        for j in i:
            if ord(j) >= ord('0') and ord(j) <= ord('9'):
                continue
            else:
                check = False
                break
        if check == True:
            ans += int(i)
    print(ans)
