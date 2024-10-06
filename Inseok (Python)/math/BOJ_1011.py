import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    N = int(math.sqrt(y - x))
    cnt = 2 * N - 1
    left = (y - x) - (N**2)
    cnt += left // N if left % N == 0 else left // N + 1

    sys.stdout.write(str(cnt) + "\n")
