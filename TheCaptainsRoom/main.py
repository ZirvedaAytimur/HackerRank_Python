k = int(input())
group = list(map(int, input().split()))
mySet = set(group)

print(((sum(mySet) * k) - sum(group)) // (k - 1))
