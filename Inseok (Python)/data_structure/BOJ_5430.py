# 새롭게 알게된 점:
# 1. strip에 문자 파라미터를 입력하고 해당 글자를 기준으로 앞뒤를 싹둑 짤라낸다
# 2. split에 문자 파라미터를 입력하고 해당 글자를 기준으로 값을 구분해서 할당한다. (csv 읽듯이)
# => 자료구조보단 문자열 지식이 부족한 것 같다.

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    comm = list(map(str, sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())
    input_ = sys.stdin.readline().strip()
    arr = deque([])
    if input_ != '[]':
        arr = deque(list(map(int, input_.strip('[]').split(','))))

   
    isValid = True
    dir = 1
    for c in comm:        
        if c == "R":
            dir = -dir
        elif c == "D":
            if arr:
                if dir == 1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                sys.stdout.write("error\n")
                isValid = False
                break
    
    if not isValid: continue
    sys.stdout.write("[")
    if dir == 1:
        for i in range(len(arr)):
            sys.stdout.write(str(arr[i]))
            if i != len(arr) - 1:
                sys.stdout.write(",")
    else:
        for i in range(len(arr) - 1, -1, -1):
            sys.stdout.write(str(arr[i]))
            if i != 0:
                sys.stdout.write(",")
    sys.stdout.write("]\n")
