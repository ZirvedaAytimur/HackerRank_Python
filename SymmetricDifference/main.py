n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

differenceAB = a.difference(b)
differenceBA = b.difference(a)
result = sorted(differenceAB.union(differenceBA))

for i in result:
    print(i)
