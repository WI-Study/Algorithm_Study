# <References>
# https://cijbest.tistory.com/14

import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())
visited = [[False] * (B + 1) for _ in range(A + 1)]
ans = []


def pour(a, b, q):
    if not visited[a][b]:
        visited[a][b] = True
        q.append((a, b))


def bfs():
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        a, b = q.popleft()
        c = C - a - b

        if a == 0:
            ans.append(c)

        water = min(a, B - b)
        pour(a - water, b + water, q)

        water = min(a, C - c)
        pour(a - water, b, q)

        water = min(b, A - a)
        pour(a + water, b - water, q)

        water = min(b, C - c)
        pour(a, b - water, q)

        water = min(c, A - a)
        pour(a + water, b, q)

        water = min(c, B - b)
        pour(a, b + water, q)


bfs()
print(" ".join(map(str, sorted(ans))))
