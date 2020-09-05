test = int(input())
for i in range(test):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))

    if A.issubset(B):
        print(True)
    else:
        print(False)
