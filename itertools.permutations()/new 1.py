from itertools import permutations

S, N = input().split()
print(*[''.join(i) for i in permutations(sorted(S), int(N))], sep="\n")