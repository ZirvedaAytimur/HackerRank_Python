n = int(input())
N = set(input().split())

b = int(input())
B = set(input().split())

print(len(N.symmetric_difference(B)))
