from collections import namedtuple

n = int(input())
arguments = input().split()
studentsList = namedtuple('student', arguments)
total = 0

for _ in range(n):
    argument1, argument2, argument3, argument4 = input().split()
    student = studentsList(argument1, argument2, argument3, argument4)
    total += int(student.MARKS)

print(format(total / n, '.2f'))
