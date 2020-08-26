from collections import OrderedDict

N = int(input())
itemDic = OrderedDict()
for _ in range(N):
    item, space, price = input().rpartition(' ')
    itemDic[item] = itemDic.get(item, 0) + int(price)

for i, j in itemDic.items():
    print(i, j)
