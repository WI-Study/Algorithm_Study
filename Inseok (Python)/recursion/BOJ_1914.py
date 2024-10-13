import sys

N = int(sys.stdin.readline())

if N > 20:
    ans = 0
    for _ in range(N):
        ans += ans + 1
    print(ans)

else:
    onepan = [[i for i in range(N, 0, -1)], [], []]
    cnt = 0
    stage = []

    def hanoi(h, s, d):
        global cnt
        r = 3 - s - d
        if h != 1:
            hanoi(h - 1, s, r)

        stage.append(f"{s + 1} {d + 1}\n")
        cnt += 1
        onepan[d].append(onepan[s].pop())

        if h != 1:
            hanoi(h - 1, r, d)

    hanoi(N, 0, 2)
    sys.stdout.write(str(cnt) + "\n")
    for s in stage:
        sys.stdout.write(s)
