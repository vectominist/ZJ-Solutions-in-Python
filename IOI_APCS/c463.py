import sys

# It is impossible to use recursion in this problem.
# Because it leads to stack overflow.
# Thus, I changed to solve it by while loop.

# sys.setrecursionlimit(100005)
s = sys.stdin.readline()
num = s.split()
n = int(num[0])

tree = []
tree.append([]) # i = 0
checkRoot = [False] * (n + 1)

for i in range(n):
    s = sys.stdin.readline()
    num = s.split()
    k = int(num[0])
    tmpList = []
    for j in range(1, k + 1):
        tmp = int(num[j])
        tmpList.append(tmp)
        checkRoot[tmp] = True
    tree.append(tmpList)

def MAX(x, y):
    if x > y:
        return x
    else:
        return y
'''
def dfs(nowNode):
    mx = 0
    ans = 0
    if len(tree[nowNode]) == 0:
        return (0, 0)
    for child in tree[nowNode]:
        tmp = dfs(child)
        mx = MAX(mx, tmp[0] + 1)
        ans += tmp[1]
    ans += mx
    return (mx, ans)
'''
root = 0
for i in range(1, n + 1):
    if checkRoot[i] == False:
        root = i
        break

# res = dfs(root)

topOrd = [root]
stack = [root]
while len(stack) > 0:
    nowNode = stack[-1]
    stack.pop()
    for child in tree[nowNode]:
        topOrd.append(child)
        stack.append(child)

topOrd.reverse()
h = [0] * (n + 1)
ans = 0
for i in topOrd:
    for child in tree[i]:
        h[i] = MAX(h[i], h[child] + 1)
    ans += h[i]

print(root)
print(ans)
