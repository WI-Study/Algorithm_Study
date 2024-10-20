import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
S, X, Y = map(int, sys.stdin.readline().split())

buff = []
for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            buff.append([r, c, 0, board[r][c]])
buff.sort(key=lambda x: x[3])
q = deque(buff)

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    cr, cc, sec, vt = q.popleft()
    if sec == S:
        break
    for d in dir:
        nr, nc = cr + d[0], cc + d[1]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
            board[nr][nc] = board[cr][cc]
            q.append([nr, nc, sec + 1, vt])

sys.stdout.write(str(board[X - 1][Y - 1]) + "\n")
