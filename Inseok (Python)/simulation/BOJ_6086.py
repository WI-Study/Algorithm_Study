import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(52)]


def stoi(ch):
    if 65 <= ord(ch) <= 90:
        return ord(ch) - 65
    else:
        return ord(ch) - 97 + 26


for _ in range(N):
    s, e, v = map(str, sys.stdin.readline().split())
    s, e, v = stoi(s), stoi(e), int(v)
    graph[s].append([e, v])


def merge(cur, vol):
    if not graph[cur]:
        if cur != 25:  # 끊어진 파이프
            return 0
        return vol

    parallel = 0
    for next in graph[cur]:
        parallel += merge(next[0], next[1])
    return min(vol, parallel)


print(merge(0, float("inf")))
