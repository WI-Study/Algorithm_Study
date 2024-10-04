import sys

N, r, c = map(int, sys.stdin.readline().split())
graph = [[0] * (2**N) for _ in range(2**N)]
cnt = 0


def z(r, c, size):
    """
    TODO:
    일일이 모든 원소를 방문하지 않고,
    꼭 방문해야 하는 곳만 찾아가도록 하는
    수학적 논리로 재구현
    (이런 거 약하단 말이야..)
    """

    global cnt
    if size > 2:
        z(r, c, size // 2)
        z(r, c + (size // 2), size // 2)
        z(r + (size // 2), c, size // 2)
        z(r + (size // 2), c + (size // 2), size // 2)
    else:
        graph[r][c] = cnt
        graph[r][c + 1] = cnt + 1
        graph[r + 1][c] = cnt + 2
        graph[r + 1][c + 1] = cnt + 3
        cnt += 4


z(0, 0, 2**N)
print(graph[r][c])
