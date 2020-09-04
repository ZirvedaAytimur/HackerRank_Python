a = int(input())
A = set(map(int, input().split()))
test = int(input())

for i in range(test):
    command, size = input().split()
    N = set(map(int, input().split()))
    eval("A." + command + "(N)")
print(sum(A))
