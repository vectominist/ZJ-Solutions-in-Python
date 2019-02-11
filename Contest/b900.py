import sys

s = sys.stdin.readline()
num = s.split()
W = int(num[0])
H = int(num[1])

rMap = []

for cnt in range(H):
    s = sys.stdin.readline()
    num = s.split()
    s = num[0]
    sMap = [0]

    for i in s:
        if i == '.':
            sMap.append(0)
        elif i == '-':
            sMap.append(1)
    sMap.append(0)
    rMap.append(sMap)

ans = []
for i in range(W):
    now = i + 1
    for h in range(H):
        if rMap[h][now] > 0:
            now += 1
        elif rMap[h][now - 1] > 0:
            now -= 1
    ans.append(now)

ansStr = ''
for i in range(W):
    if i == 0:
        ansStr += str(ans[i])
    else:
        ansStr += ' ' + str(ans[i])

print(ansStr)
