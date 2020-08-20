if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    scores = list(set([students[x][1] for x in range(len(students))]))
    scores.sort()

    students = [x[0] for x in students if x[1] == scores[1]]
    students.sort()

    for i in students:
        print(i)