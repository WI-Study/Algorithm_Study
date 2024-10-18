import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()

# nlogn
ans = A[N - 1] - A[0]
for i in range(N - 1):
    l = i + 1
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] - A[i] >= M:
            ans = min(ans, A[mid] - A[i])
            r = mid - 1
        else:
            l = mid + 1

print(ans)
