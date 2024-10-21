# <References>
# https://baby-ohgu.tistory.com/17

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(a[0])
    sys.exit()

dp = [[0] * n for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = a[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + a[i], a[i])  # 삭제하지 않은 경우
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + a[i], a[i])  # 삭제한 경우

print(max(max(dp[0]), max(dp[1])))
