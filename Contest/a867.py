import sys

dx = [0,  0, 1, 1,  1, -1, -1, -1]
dy = [1, -1, 1, 0, -1,  1,  0, -1]

for s in sys.stdin:
    if s == '\n':
        continue
    mp = []
    for i in range(17):
        mp.append([0] * 32)
    

    for i in range(1, 16):
        if i > 1:
            s = sys.stdin.readline()
        for j in range(1, 31):
            if s[j - 1] == '*':
                mp[i][j] = -1
                for k in range(8):
                    if mp[i + dx[k]][j + dy[k]] != -1:
                        mp[i + dx[k]][j + dy[k]] += 1
        
    for i in range(1, 16):
        ans = ''
        for j in range(1, 31):
            if mp[i][j] == 0:
                ans += '.'
            elif mp[i][j] == -1:
                ans += '*'
            else:
                ans += str(mp[i][j])
        print(ans)
