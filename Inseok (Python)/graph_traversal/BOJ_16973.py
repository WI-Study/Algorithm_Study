import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())

visited = [[-1] * M for _ in range(N)]
visited[Sr - 1][Sc - 1] = 0
q = deque([(Sr - 1, Sc - 1)])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
while q:
    cr, cc = q.popleft()
    for i in range(4):
        nr, nc = cr + dr[i], cc + dc[i]
        if 0 <= nr + H - 1 < N and 0 <= nc + W - 1 < M and 0 <= nr and 0 <= nc:
            if visited[nr][nc] == -1:
                isValid = True
                if 0 <= i <= 1:
                    r = nr + H - 1 if i == 0 else nr
                    for c in range(nc, min(M, nc + W)):
                        if graph[r][c] == 1:
                            isValid = False
                            break
                else:
                    c = nc + W - 1 if i == 2 else nc
                    for r in range(nr, min(N, nr + H)):
                        if graph[r][c] == 1:
                            isValid = False
                            break

                if isValid:
                    visited[nr][nc] = visited[cr][cc] + 1
                    if nr == Fr - 1 and nc == Fc - 1:
                        print(visited[nr][nc])
                        sys.exit(0)
                    q.append([nr, nc])

print(-1)
