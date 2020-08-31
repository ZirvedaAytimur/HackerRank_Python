n = int(input())
s = set(map(int, input().split()))
operations = int(input())

for i in range(operations):
    command = list(map(str, input().split(" ")))
    if command[0] == 'pop':
        s.pop()
    else:
        eval("s." + command[0] + "(" + command[1] + ")")

print(sum(s))
