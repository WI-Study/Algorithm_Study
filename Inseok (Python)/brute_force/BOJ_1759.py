import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
char = sorted(list(map(str, sys.stdin.readline().split())))
case = list(combinations(char, L))


def isValid(c):
    ja, mo = 0, 0
    for a in c:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
            mo += 1
        else:
            ja += 1

    if ja >= 2 and mo >= 1:
        return True
    return False


for c in case:
    if isValid(c):
        sys.stdout.write("".join(c) + "\n")
