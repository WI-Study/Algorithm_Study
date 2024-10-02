# <References>
# https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-2504%EB%B2%88-%EA%B4%84%ED%98%B8%EC%9D%98-%EA%B0%92-python-stack-%EC%9E%90%EC%84%B8%ED%95%9C-%ED%92%80%EC%9D%B4

import sys

str = list(map(str, sys.stdin.readline().strip()))
stack = []

ans = 0
temp = 1

# 단는 괄호를 만났을 때, 직전 게 그 괄호에 맞는 쌍일 경우
# 가장 내부까지 파고 들어갔다고 인식하고 버퍼에 쌓인 값을 ans에 집어넣는다는 것이 핵심.
# => 여기서 이때까지 쌓인 껍질 수까지 다 고려해서 한번에 다 쌓인다. (temp에 거듭제곱하면서 다 계산해놨음)
# 그렇지 않을 경우 가장 쏙알맹이가 아니기 때문에 소거만 한다. (껍질이 그저 벗겨지는 과정)

for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
        temp *= 2
    elif str[i] == "[":
        stack.append(str[i])
        temp *= 3
    elif str[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if str[i - 1] == "(":
            ans += temp
        stack.pop()
        temp //= 2  # 차츰 되들림
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if str[i - 1] == "[":
            ans += temp
        stack.pop()
        temp //= 3  # 차츰 되들림

if stack:
    print(0)
else:
    print(ans)
