#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            result_matrix[i][k] = matrix[i][k] ** 2

    return result_matrix
