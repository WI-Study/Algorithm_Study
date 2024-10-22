import sys
from collections import deque

N = int(sys.stdin.readline())

rel = [[] for _ in range(N + 1)]
while True:
    eg, zg = map(int, sys.stdin.readline().split())
    if eg == -1 and zg == -1:
        break

    # EG! and ZG! are good friends~
    rel[eg].append(zg)
    rel[zg].append(eg)


def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([(start, 0)])
    score = 0

    while q:
        cp, cs = q.popleft()
        for next in rel[cp]:
            if not visited[next]:
                visited[next] = True
                q.append([next, cs + 1])
                score = max(score, cs + 1)

    return score


candidate = []
for i in range(1, N + 1):
    candidate.append([i, bfs(i)])

candidate.sort(key=lambda x: x[1])
ans1 = [candidate[0][1], 0]
ans2 = []
for c in candidate:
    if c[1] != ans1[0]:
        break
    ans1[1] += 1
    ans2.append(c[0])

sys.stdout.write(" ".join(map(str, ans1)) + "\n")
sys.stdout.write(" ".join(map(str, ans2)) + "\n")
