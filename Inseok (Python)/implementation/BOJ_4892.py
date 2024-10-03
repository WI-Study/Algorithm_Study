import sys

t = 0
while True:
    t += 1
    n0 = int(sys.stdin.readline())
    if n0 == 0:
        break

    n1 = n0 * 3
    n2 = n1 // 2 if n1 % 2 == 0 else (n1 + 1) // 2
    n3 = n2 * 3
    n4 = n3 // 9
    mid = "odd" if n1 % 2 == 1 else "even"
    sys.stdout.write(f"{t}. {mid} {n4}\n")
