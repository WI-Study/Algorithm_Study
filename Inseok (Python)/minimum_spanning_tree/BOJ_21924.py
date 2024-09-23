import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
line = []
for _ in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))
line.sort(key=lambda x: x[2])


def find(a):
    while parent[a] != a:
        a = parent[a]
    return a


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


total = 0
cost = 0
connected = 0
for l in line:
    total += l[2]
    if union(l[0], l[1]):
        connected += 1
        cost += l[2]

ans = total - cost if connected == N - 1 else -1
print(ans)
