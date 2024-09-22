# <References>
# https://minny27.tistory.com/42

import sys
from collections import deque

sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * N for _ in range(N)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]

    dp[r][c] = 1
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > graph[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

    return dp[r][c]


ans = 1
for r in range(N):
    for c in range(N):
        if dp[r][c] == 0:
            ans = max(ans, dfs(r, c))

print(ans)
