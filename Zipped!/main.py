n, x = input().split()

exams = []
for i in range(int(x)):
    exams.append(map(float, input().split()))

for i in zip(*exams):
    print(sum(i) / len(i))
