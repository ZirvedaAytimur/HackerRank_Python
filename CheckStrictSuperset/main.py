A = set(map(int, input().split()))
test = int(input())
check = True
for i in range(test):
    B = set(map(int, input().split()))
    if A.issuperset(B) is False:
        check = False
        break

print(check)
