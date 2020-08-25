from collections import defaultdict
d = defaultdict(list)
searchFor = []

n, m = map(int, input().split())

for i in range(n):
    d[input()].append(i + 1)

for i in range(m):
    searchFor.append(input())

for i in searchFor:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print("-1")