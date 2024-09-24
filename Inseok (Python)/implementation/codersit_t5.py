import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
l1, l2, l3 = map(int, sys.stdin.readline().split())
l1 -= 1
l2 -= 1
l3 -= 1

l = [0] * N
l[l1] = 1
l[l2] = 1
l[l3] = 1

for p in (l1, l2, l3):
    for i in range(1, K + 1):
        if p - i >= 0:
            l[p - i] = 1
    for i in range(1, K + 1):
        if p + i < N:
            l[p + i] = 1

sys.stdout.write(str(sum(l)) + "\n")
