import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

d = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
order = []
for _ in range(M):
    order.append(list(map(int, sys.stdin.readline().split())))

cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
banned = [[False] * N for _ in range(N)]

for o in order:
    wet = []
    while cloud:
        c = cloud.pop()
        c[0], c[1] = (c[0] + d[o[0]][0] * o[1]) % N, (c[1] + d[o[0]][1] * o[1]) % N
        wet.append([c[0], c[1]])
        banned[c[0]][c[1]] = True
        board[c[0]][c[1]] += 1

    for w in wet:
        for i in (2, 4, 6, 8):
            nr, nc = w[0] + d[i][0], w[1] + d[i][1]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > 0:
                board[w[0]][w[1]] += 1

    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2:
                if not banned[r][c]:
                    cloud.append([r, c])
                    board[r][c] -= 2
                else:
                    banned[r][c] = False

ans = 0
for b in board:
    ans += sum(b)
print(ans)
