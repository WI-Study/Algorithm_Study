# <References>
# https://www.acmicpc.net/board/view/147180

import sys

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))

arr = [0] * 1000001         # 공중에 떠 있는 화살의 개수
ans = 0
for h in H:
    if arr[h] == 0:         # 날라오고 있는 화살이 없는 경우
        arr[h - 1] += 1     # 화살을 하나 새로 쏘고 풍선을 터뜨린 다음, 높이를 1 낮춘다.
        ans += 1
    else:                   # 이전에 날린 화살이 이미 존재한다.
        arr[h] -= 1         # 그 화살을 사용한다. 그러면 높이가 1 줄어들 것이다.
        arr[h - 1] += 1     

print(ans)
