import sys

MAXN = 1000005

def get_sqr_sum(x):
    ans = 0
    while x > 0:
        ans += (x % 10) ** 2
        x //= 10
    return ans

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    used = [False] * MAXN
    if n < MAXN:
        used[n] = True
    tmpN = n
    ans = False
    while True :
        tmpN = get_sqr_sum(tmpN)
        if tmpN == 1:
            ans = True
            break
        elif tmpN < MAXN:
            if used[tmpN] == True:
                break
            else:
                used[tmpN] = True

    if ans == True:
        print('%d is a happy number' % (n))
    else:
        print('%d is an unhappy number' % (n))
