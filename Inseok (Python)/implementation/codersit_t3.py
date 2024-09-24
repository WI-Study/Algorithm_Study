import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
K = int(sys.stdin.readline())

for _ in range(K):
    C, D = map(int, sys.stdin.readline().split())
    A -= C
    A = A + D if A + D <= N else N

sys.stdout.write(str(A) + "\n")
