import re

test = int(input())

for _ in range(test):
    answer = True
    try:
        regular = re.compile(input())
    except re.error:
        answer = False
    print(answer)