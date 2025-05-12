#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(0, len(i)):
            if j < len(i) - 1:
                print("{:d}" .format(i[j]), end=" ")
            else:
                print("{:d}" .format(i[j]), end="")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
