import sys
# import math
# import numpy as np

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    for i in range(n):
        print('_' * (n - i - 1) + '*' * (2 * i + 1) + '_' * (n - i - 1))
