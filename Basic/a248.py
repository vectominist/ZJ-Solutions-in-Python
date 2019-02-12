import sys

# Big Number Division with Precision N
def fast_pow(x, n):
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x = x ** 2
        n >>= 1
    return res

def digits(x):
    res = 0
    while x > 0:
        res += 1
        x //= 10
    return res

for s in sys.stdin:
    num = s.split()
    a = int(num[0])
    b = int(num[1])
    N = int(num[2])
    c = fast_pow(10, N) * a // b
    ans = str(c)

    if len(ans) < N:
        tmpS = '0' * (N - len(ans))
        ans = '0.' + tmpS + ans
    elif len(ans) == N:
        ans = '0.' + ans
    else:
        n = digits(a // b)
        ans = ans[:n] + '.' + ans[n:]

    print(ans)

