#!/usr/bin/env python
import sys
from concurrent.futures import ProcessPoolExecutor

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        row, col, value = line.rstrip().split(",")
        data.append((int(row), int(col), float(value)))
    return data

def process_line(line, row_col, is_matrix_a):
    results = []
    row, col, value = line
    if is_matrix_a:
        for i in range(0, row_col):
            key = str(row) + "," + str(i)
            results.append("{}\t{}\t{}".format(key, col, value))
    else:
        for j in range(0, row_col):
            key = str(j) + "," + str(col)
            results.append("{}\t{}\t{}".format(key, row, value))
    return results

def process_input(matrix_a, matrix_b):
    row_a = max([row for row, col, value in matrix_a]) + 1
    col_b = max([col for row, col, value in matrix_b]) + 1

    with ProcessPoolExecutor() as executor:
        results_a = list(executor.map(process_line, matrix_a, [col_b]*len(matrix_a), [True]*len(matrix_a)))
        results_b = list(executor.map(process_line, matrix_b, [row_a]*len(matrix_b), [False]*len(matrix_b)))

    for result in results_a + results_b:
        for line in result:
            print(line)

if __name__ == "__main__":
    matrix_a_file = sys.argv[1]
    matrix_b_file = sys.argv[2]

    matrix_a = read_file(matrix_a_file)
    matrix_b = read_file(matrix_b_file)
    process_input(matrix_a, matrix_b)