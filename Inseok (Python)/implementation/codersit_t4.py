import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
req = list(map(int, sys.stdin.readline().split()))

ans = 0
for _ in range(M):
    mine = list(map(int, sys.stdin.readline().split()))
    isValid = True
    for i in range(N):
        if mine[i] < req[i]:
            isValid = False
            break

    if isValid:
        ans += 1

sys.stdout.write(str(ans) + "\n")
