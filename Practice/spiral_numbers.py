import sys
# import math
import numpy as np

def solve(n):
    w = 2 * n - 1  # width
    matrix = np.zeros((w + 2, w + 2), dtype = int)
    m = (w + 1) >> 1  # mid
    matrix[m][m] = 1
    cnt = 2
    for i in range(1, n):
        w2 = 2 * i
        for j in range(1, w2 + 1):
            matrix[m + i - j][m + i] = cnt
            cnt += 1
        
        for j in range(1, w2 + 1):
            matrix[m + i - w2][m + i - j] = cnt
            cnt += 1
        
        for j in range(1, w2 + 1):
            matrix[m + i - w2 + j][m + i - w2] = cnt
            cnt += 1
        
        for j in range(1, w2 + 1):
            matrix[m + i][m + i - w2 + j] = cnt
            cnt += 1
    
    check_len = len(str(w ** 2))
    for i in range(1, w + 1):
        ans = ''
        for j in range(1, w + 1):
            nStr = str(matrix[i][j])
            nStr = (' ' * (check_len - len(nStr))) + nStr
            if j == 1:
                ans += nStr
            else:
                ans += ' ' + nStr
        print(ans)
    
    return

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    solve(n)
