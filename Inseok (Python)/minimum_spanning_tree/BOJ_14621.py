import sys

N, M = map(int, sys.stdin.readline().split())
gender = list(map(str, sys.stdin.readline().split()))

line = []
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if gender[u - 1] != gender[v - 1]:
        line.append([u, v, d])
line.sort(key=lambda x: x[2])


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    A, B = find(a), find(b)
    if A == B:
        return False

    if rank[A] > rank[B]:
        parent[B] = A
    elif rank[A] < rank[B]:
        parent[A] = B
    else:
        parent[B] = A
        rank[A] += 1

    return True


ans = 0
connected = 0
for l in line:
    if union(l[0], l[1]):
        ans += l[2]
        connected += 1

if connected == N - 1:
    print(ans)
else:
    print(-1)
