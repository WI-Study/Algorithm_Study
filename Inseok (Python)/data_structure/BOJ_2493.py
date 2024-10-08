import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
ans = [0] * N

stack = []
for i in range(N - 1, -1, -1):
    while stack and top[i] > top[stack[-1]]:
        ans[stack.pop()] = i + 1
    stack.append(i)

print(" ".join(map(str, ans)))
