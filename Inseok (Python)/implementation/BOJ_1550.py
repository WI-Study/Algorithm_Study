import sys

h = list(map(str, sys.stdin.readline().strip()))
ans = 0
for i in range(len(h)):
    asc = ord(h[(-i - 1)])
    if 48 <= asc <= 57:
        ans += (asc - 48) * (16**i)
    else:
        ans += (asc - 55) * (16**i)

print(ans)