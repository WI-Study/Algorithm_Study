import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
T = int(sys.stdin.readline())

t1 = 0 if T - 30 < 0 else T - 30
t2 = 0 if T - 45 < 0 else T - 45

f1 = A + 21 * B * t1
f2 = C + 21 * D * t2

sys.stdout.write(f"{f1} {f2}\n")
