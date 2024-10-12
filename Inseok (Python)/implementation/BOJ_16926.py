import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


def circular(start_r, start_c, size_n, size_m):
    global arr
    ring = []
    end_r, end_c = start_r + size_n - 1, start_c + size_m - 1
    for c in range(start_c, end_c + 1):  # RIGHT
        ring.append(arr[start_r][c])
    for r in range(start_r + 1, end_r + 1):  # DOWN
        ring.append(arr[r][end_c])
    for c in range(end_c - 1, start_c - 1, -1):  # LEFT
        ring.append(arr[end_r][c])
    for r in range(end_r - 1, start_r, -1):  # UP
        ring.append(arr[r][start_c])

    i = R % len(ring)
    for c in range(start_c, end_c + 1):  # RIGHT
        arr[start_r][c] = ring[i]
        i = (i + 1) % len(ring)
    for r in range(start_r + 1, end_r + 1):  # DOWN
        arr[r][end_c] = ring[i]
        i = (i + 1) % len(ring)
    for c in range(end_c - 1, start_c - 1, -1):  # LEFT
        arr[end_r][c] = ring[i]
        i = (i + 1) % len(ring)
    for r in range(end_r - 1, start_r, -1):  # UP
        arr[r][start_c] = ring[i]
        i = (i + 1) % len(ring)


for i in range(min(N, M) // 2):
    circular(i, i, N - (2 * i), M - (2 * i))

for row in arr:
    sys.stdout.write(" ".join(map(str, row)))
    sys.stdout.write("\n")
