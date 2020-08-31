from itertools import combinations_with_replacement

S, k = input().split()

S = sorted(S)
for i in list(combinations_with_replacement(S, int(k))):
    print("".join(i))
