import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = list(map(str, sys.stdin.readline().strip()))

    def check(l, r, isDel):
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                if not isDel:
                    if check(l + 1, r, True) == 0 or check(l, r - 1, True) == 0:
                        return 1
                    else:
                        return 2
                else:
                    return 2

        return 0

    sys.stdout.write(str(check(0, len(s) - 1, 0)) + "\n")
