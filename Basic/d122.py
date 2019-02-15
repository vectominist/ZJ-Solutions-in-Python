import sys

mul = [1, 5]
for i in range(2, 28):
    mul.append(mul[i - 1] * 5)

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    ans = 0
    for i in range(1, 28):
        if mul[i] > n:
            break
        else:
            ans += (n // mul[i])
    print(ans)

