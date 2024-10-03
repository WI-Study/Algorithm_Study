import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x < y:
        sys.stdout.write("NO BRAINS\n")
    else:
        sys.stdout.write("MMM BRAINS\n")
