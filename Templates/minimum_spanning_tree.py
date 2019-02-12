import sys

# union find tree
MAXN = 100005
n = 0
m = 0
par = [0] * MAXN
rk = [0] * MAXN

def initialize():
    for i in range(n):
        par[i] = i
        rk[i] = 0

def findx(x):
    if par[x] != x:
        par[x] = findx(par[x])
    return par[x]

def unite(a, b):
    a = findx(a)
    b = findx(b)
    if a == b:
        return
    if rk[a] < rk[b]:
        par[a] = b
    else:
        if rk[a] == rk[b]:
            rk[a] += 1
        par[b] = a

def same(a, b):
    return findx(a) == findx(b)


for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    m = int(num[1])

    if m == 0 and n == 1:
        print('0')
        continue
    elif m == 0 and n > 1:
        print('-1')
        continue

    graph = []
    for i in range(m):
        s = sys.stdin.readline()
        num = s.split()
        graph.append((int(num[2]), int(num[0]), int(num[1])))
        # (weight, vertex 1, vertex 2)

    graph.sort()
    '''for i in graph:
        print(i)'''
    initialize()
    ans = 0
    for i in graph:
        if same(i[1], i[2]) == False:
            ans += i[0]
            unite(i[1], i[2])
    
    for i in range(1, n):
        if same(0, i) == False:
            ans = -1
    
    print(ans)
