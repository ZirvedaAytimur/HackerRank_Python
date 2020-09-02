from itertools import product

K, M = [int(x) for x in input().split()]
arrayN = []
for i in range(K):
    arrayN.append([int(x) for x in input().split()][1:])

possible_combination = list(product(*arrayN))

def func(nums):
    return sum(x * x for x in nums) % M

print(max(list(map(func, possible_combination))))