import sys

s = sys.stdin.readline()

for i in range(5):
    s = sys.stdin.readline()
    num = s.split()
    a = []
    a.append(int(num[0]))
    a.append(int(num[1]))
    a.append(int(num[2]))
    print(max(a))
