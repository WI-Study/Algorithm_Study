import sys

W, H = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
    graph.append(list(map(str, sys.stdin.readline().strip())))

for c in range(W):
    for r in range(H - 1, -1, -1):
        if graph[r][c] == "*":
            nr = r + 1
            while nr < H and graph[nr][c] == ".":
                nr += 1
            graph[nr - 1][c] = "*"
            if nr - 1 != r:
                graph[r][c] = "."

for row in graph:
    sys.stdout.write("".join(row))
    sys.stdout.write("\n")
