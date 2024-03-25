#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            end = " " if (j != i[len(i) - 1]) else ""
            print("{:d}".format(j), end=end)
        print()
