import sys

for s in sys.stdin:
    if s == '\n':
        continue
    s = s.split()
    if s[0] == 'END':
        break
    ans = ''
    for i in s:
        ans += str(chr(ord(i[0]) - ord('a') + ord('A')))
    ans += ' ' + s[-1]
    print(ans)

