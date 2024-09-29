import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs():
    visited = [[[float("inf"), float("inf")] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 0
    q = deque([(0, 0, 0)])

    while q:
        cr, cc, gram = q.popleft()
        for d in dir:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc][gram] == float("inf"):
                    if graph[nr][nc] != 1 or (graph[nr][nc] == 1 and gram):
                        if graph[nr][nc] == 2:
                            visited[nr][nc][0] = visited[cr][cc][0] + 1
                            visited[nr][nc][1] = visited[cr][cc][0] + 1
                            q.append([nr, nc, 1])
                        else:
                            visited[nr][nc][gram] = visited[cr][cc][gram] + 1
                            q.append([nr, nc, gram])

    return min(visited[N - 1][M - 1])


result = bfs()
if result == -1 or result > T:
    print("Fail")
else:
    print(result)
