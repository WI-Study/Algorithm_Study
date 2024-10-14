import sys

N, H = map(int, sys.stdin.readline().split())

stick = [[], []]
turn = 0
for _ in range(N):
    stick[turn].append(int(sys.stdin.readline()))
    turn = 1 - turn

stick[0].sort()
stick[1].sort()

col1 = [0] * (H + 1)
for i in range(len(stick[0])):
    if col1[stick[0][i]] == 0:
        col1[stick[0][i]] = len(stick[0]) - i
cur = col1[-1]
for i in range(len(col1) - 1, -1, -1):
    if col1[i] == 0:
        col1[i] = cur
    else:
        cur = col1[i]

col2 = [0] * (H + 1)
for i in range(len(stick[1])):
    if col2[H + 1 - stick[1][i]] == 0:
        col2[H + 1 - stick[1][i]] = len(stick[1]) - i
cur = col2[0]
for i in range(len(col2)):
    if col2[i] == 0:
        col2[i] = cur
    else:
        cur = col2[i]

col = [col1[i] + col2[i] for i in range(1, H + 1)]
col.sort()

ans1 = col[0]
ans2 = 0
for c in col:
    if c != ans1:
        break
    ans2 += 1

print(f"{ans1} {ans2}")
