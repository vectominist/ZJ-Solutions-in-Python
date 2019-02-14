import sys

s = sys.stdin.readline()
s = s.split()
string = s[0]

ans = string[0] + '_' * (len(string) - 2) + string[-1]
print(ans)
