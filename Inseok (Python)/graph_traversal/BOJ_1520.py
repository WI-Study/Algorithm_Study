import sys

sys.setrecursionlimit(10**8)

M, N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

# dp[r][c]: r, c에서 목표 지점까지 가는 지금까지 알아낸 경로의 개수
dp = [[-1] * N for _ in range(M)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < M and 0 <= nc < N and graph[r][c] > graph[nr][nc]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]


print(dfs(0, 0))
