import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = [] if M == 0 else list(map(int, sys.stdin.readline().split()))


def canMove(ch):
    for num in str(ch):
        if (int(num)) in broken:
            return False
    return True


ans = abs(N - 100)
for i in range(1000001):
    if canMove(i):
        ans = min(ans, len(str(i)) + abs(N - i))

print(ans)
