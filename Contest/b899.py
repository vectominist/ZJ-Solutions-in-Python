import sys

def DOT(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

cor = []

for i in range(3):
    s = sys.stdin.readline()
    num = s.split()
    cor.append((int(num[0]), int(num[1])))

vec1 = (cor[1][0] - cor[0][0], cor[1][1] - cor[0][1])
vec2 = (cor[2][0] - cor[0][0], cor[2][1] - cor[0][1])
ans = (0, 0)

if DOT(vec1, vec2) != 0:
    vec1 = (cor[0][0] - cor[1][0], cor[0][1] - cor[1][1])
    vec2 = (cor[2][0] - cor[1][0], cor[2][1] - cor[1][1])
    if DOT(vec1, vec2) != 0:
        vec1 = (cor[0][0] - cor[2][0], cor[0][1] - cor[2][1])
        vec2 = (cor[1][0] - cor[2][0], cor[1][1] - cor[2][1])
        ans = (cor[2][0] + vec1[0] + vec2[0], cor[2][1] + vec1[1] + vec2[1])
    else:
        ans = (cor[1][0] + vec1[0] + vec2[0], cor[1][1] + vec1[1] + vec2[1])
else:
    ans = (cor[0][0] + vec1[0] + vec2[0], cor[0][1] + vec1[1] + vec2[1])

print('%d %d' % (ans[0], ans[1]))
