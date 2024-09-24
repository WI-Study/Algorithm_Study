import sys

N = int(sys.stdin.readline())

# 나머지 0 => 3인실 몰빵
# 나머지 1 => 2인실 2개, 나머지 다 3인실
# 나머지 2 => 2인실 1개, ""

if N % 3 == 0:
    sys.stdout.write(f"0 {N // 3}\n")
elif N % 3 == 1:
    sys.stdout.write(f"2 {(N - 4) // 3}\n")
else:
    sys.stdout.write(f"1 {(N - 2) // 3}\n")
