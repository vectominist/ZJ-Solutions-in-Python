import sys

cnt = [0] * 6
N = 0

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n == 0:
        break
    cnt[n] += 1
    N += 1

total = 0
for i in range(5, 0, -1):
    total += cnt[i] * i
    ans = str(i) + ' ('
    if cnt[i] < 10:
        ans += ' '
    ans += str(cnt[i]) + ') |'
    ans += '=' * cnt[i]
    print(ans)

print('Average rating: %.4lf' % (float(total) / float(N)))
