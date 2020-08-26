n, m = input().split()

searchFor = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0

for i in range(int(n)):
    if searchFor[i] in A:
        happiness += 1
    elif searchFor[i] in B:
        happiness -= 1

print(happiness)
