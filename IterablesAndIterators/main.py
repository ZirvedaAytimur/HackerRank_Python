from itertools import combinations

_ = int(input())
N = list(map(str, input().split()))
K = int(input())

comb = list(combinations(N, K))
pos = [i for i in comb if 'a' in i]

print("{0:.4f}".format(len(pos) / len(comb)))
