import sys

fib = [1, 1, 2]
for i in range(3, 100):
    fib.append(fib[-1] + fib[-2])

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    print(fib[n])
