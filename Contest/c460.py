import sys

s = sys.stdin.readline()
num = s.split()
N = int(num[0])

dp = []
for i in range(8):
    dp.append([0] * 8)

for i in range(N):
    s = sys.stdin.readline()
    num = s.split()
    ctype = int(num[0])
    if ctype == 3:
        ctype = 4
    atype = int(num[1])
    rtype = int(num[2])
    dtype = int(num[3])
    feature = (atype << 2) + (rtype << 1) + (dtype)
    dp[ctype][feature] += 1

for c in range(3, 8):
    if c == 4:
        continue
    for c1 in range(8):
        for c2 in range(c1, 8):
            if ((c1 | c2) == c) and (c1 & c2 == 0):
                for f1 in range(8):
                    for f2 in range(8):
                        dp[c][f1 | f2] += dp[c1][f1] * dp[c2][f2]
                        
# calculations in dp: 640 updates
print(dp[7][7] // 3)

