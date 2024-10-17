import sys

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    h.append(int(sys.stdin.readline()))

ans = 0
stack = []
for b in h:
    while stack and stack[-1] <= b:
        stack.pop()
    if stack and stack[-1] > b:
        ans += len(stack)
    stack.append(b)

print(ans)
