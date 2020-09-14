import re


test = int(input())

for i in range(test):
    N = input()
    print(bool(re.search(r"^[+-]?\d*\.\d+$", N)))
