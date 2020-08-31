from _collections import deque

N = int(input())
d = deque()

for i in range(N):
    command = list(map(str, input().split(' ')))

    if len(command) == 1:
        eval("d." + command[0] + "()")

    else:
        eval("d." + command[0] + "(" + command[1] + ")")

print(*d)
