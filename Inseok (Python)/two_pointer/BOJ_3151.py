# 중복 값에 대한 처리 미흡

import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

ans = 0
for m in range(1, N - 1):
    l, r = 0, N - 1
    while l < m < r:
        if A[l] + A[m] + A[r] == 0:
            ol_, or_ = l, r
            print(f"l: {l}, m: {m}, r: {r},")
            ans += 1
            while l + 1 < m < r and A[l + 1] + A[m] + A[r] == 0:
                l += 1
                print(f"l: {l}, m: {m}, r: {r},")
                ans += 1
                l = ol_
            while l < m < r - 1 and A[l] + A[m] + A[r - 1] == 0:
                r -= 1
                print(f"l: {l}, m: {m}, r: {r},")
                ans += 1
            break

        elif A[l] + A[m] + A[r] < 0:
            l += 1
        else:
            r -= 1

print(ans)
