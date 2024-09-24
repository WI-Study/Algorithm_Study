import sys

W, H = map(int, sys.stdin.readline().split())
visited = [[False] * W for _ in range(H)]
graph = []
for _ in range(H):
    graph.append(list(map(str, sys.stdin.readline().strip())))

d = {"D": [1, 0], "U": [-1, 0], "R": [0, 1], "L": [0, -1]}
cr, cc = 0, 0

ans = ""
moves = 0
while True:
    visited[cr][cc] = True
    if graph[cr][cc] == "T":
        ans = str(moves)
        break
    nr, nc = cr + d[graph[cr][cc]][0], cc + d[graph[cr][cc]][1]
    if 0 <= nr < H and 0 <= nc < W:
        if visited[nr][nc]:
            ans = "lost"
            break
        else:
            moves += 1
            cr, cc = nr, nc
    else:
        ans = "out"
        break

sys.stdout.write(ans + "\n")
