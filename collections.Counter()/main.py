from collections import Counter

_ = int(input())

myList = list(map(int, input().split()))

customers = int(input())
sum = 0
for i in range(customers):
    counter = Counter(myList)
    shoeSize = list(map(int, input().split()))
    if shoeSize[0] in counter.keys():
        sum += shoeSize[1]
        myList.remove(shoeSize[0])

print(sum)