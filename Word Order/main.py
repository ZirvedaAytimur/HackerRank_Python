n = int(input())

thisDict = dict()

for i in range(n):
    word = input()

    if word in thisDict:
        thisDict[word] += 1
    else:
        thisDict[word] = 1

print(len(thisDict))
print(*thisDict.values())
