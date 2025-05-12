#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in range(len(i)):
                if j < len(i) - 1:
                    print("{:d}" .format(i[j]), end=" ")
                else:
                    print("{:d}" .format(i[j]))
            print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
