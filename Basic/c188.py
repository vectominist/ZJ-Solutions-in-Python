import sys

def MIN(x, y):
    if x < y:
        return x
    else:
        return y

dp = []
for i in range(201):
    dp.append([0] * 201)
P = [0] * 201
P[0] = 1
P[1] = 1

dp[0][0] = 1
dp[1][1] = 1
for i in range(2, 201):
    for j in range(1, i + 1):
        mxk = MIN(i - j, j)
        for k in range(mxk + 1):
            dp[i][j] += dp[i - j][k]
        
        P[i] += dp[i][j]

for s in sys.stdin:
    if s == '\n':
        continue
    s = s.split()
    n = int(s[0])
    print(P[n])

