#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for row in range(len(col)):
            print('{:d}{}'.format(col[row], " "
                  if row != len(col) - 1 else ""), end="")
        print()
