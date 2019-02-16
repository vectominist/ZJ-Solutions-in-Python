import sys

for s in sys.stdin:
    num = s.split()
    A = []
    for i in num:
        A.append(int(i))
    A.sort()
    i = 0
    while i < len(A):
        j = i + 1
        while j < len(A):
            if A[j] != A[i]:
                break
            j += 1
        if (j - i) % 3 != 0:
            print(A[i])
            break
        else:
            i = j
    
