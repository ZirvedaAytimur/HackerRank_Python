test = int(input())

for _ in range(test):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as error:
        print("Error Code: ", error)