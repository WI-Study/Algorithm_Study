import sys
from itertools import combinations

max_len = 11
desc = []
arr = [i for i in range(10)]
for len_ in range(1, max_len):
    case = list(combinations(arr, len_))
    for element in case:
        desc.append(int("".join(map(str, element[::-1]))))
desc.sort()

N = int(sys.stdin.readline())
ans = -1 if N >= len(desc) else desc[N]
print(ans)
