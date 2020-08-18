import numpy

A = numpy.array(input().split(), float)
B = int(input())

print(numpy.polyval(A, B))