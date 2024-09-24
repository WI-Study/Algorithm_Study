import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(num, dest):
    moves = [-1] * (N + 1)
    moves[num] = 0
    q = deque([num])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt == dest:
                return moves[cur] + 1
            if moves[nxt] == -1:
                moves[nxt] = moves[cur] + 1
                q.append(nxt)

    return -1


K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(bfs(a, b)) + "\n")
