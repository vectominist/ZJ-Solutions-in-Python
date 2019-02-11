import sys

s = sys.stdin.readline()
num = s.split()
N = int(num[0])

S = [0] * N
for i in range(N):
    S[i] = int(num[i + 1])
S.sort()

ans = True
for i in range(N - 1):
    if S[i] + 1 != S[i + 1]:
        ans = False
        break

if ans == True:
    print('%d %d yes' % (S[0], S[N - 1]))
else:
    print('%d %d no' % (S[0], S[N - 1]))
