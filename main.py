import sys
import pandas as pd
import pathlib

dirGr = str(pathlib.Path().resolve()) 

def print_matrix(title, A):
    print(f"{title}\t" * int(len(A) / 2))
    for i in range(len(A)):
        line = ['{0:+7.3f}'.format(x) for x in A[i]]
        print(line, '\t')
    print('\n\n')

def multiply_matrices(A, B):
    rows_A = len(A)
    columns_A = len(A[0])
    rows_B = len(B)
    columns_B = len(B[0])

    if columns_A != rows_B:
        print('The number of columns in the first matrix must be equal to the number of rows in the second matrix')
        sys.exit()

    result_matrix = []
    for outer_index in range(rows_A):
        result_matrix.append([])
        for inner_index in range(columns_B):
            result_matrix[-1].append(0.0)

    for outer_index in range(rows_A):
        for inner_index in range(columns_B):
            total = 0
            for inner_index2 in range(columns_A):
                total += A[outer_index][inner_index2] * B[inner_index2][inner_index]
            result_matrix[outer_index][inner_index] = total
    columns_result_matrix = len(result_matrix[0])

    return result_matrix, columns_result_matrix

def identity_matrix(size):
    matrix = []
    for i in range(size):
        row = [0] * size
        row[i] = 1
        matrix.append(row)

    return matrix

def matrix_inverse(matrix, identity_matrix):

    size = len(matrix)

    for column in range(size):
        pivot = matrix[column][column]
        for k in range(size):
            matrix[column][k] = matrix[column][k] / pivot
            identity_matrix[column][k] = identity_matrix[column][k] / pivot

        for row in range(size):
            if row != column:
                m = matrix[row][column]
                for k in range(size):
                    matrix[row][k] = matrix[row][k] - (m * matrix[column][k])
                    identity_matrix[row][k] = identity_matrix[row][k] - (m * identity_matrix[column][k])

    return identity_matrix

def least_squares(A, b):
    A_transposed = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    A_transposed_A = multiply_matrices(A_transposed, A)[0]
    A_transposed_b = multiply_matrices(A_transposed, b)[0]
    columns_A_transposed_A = multiply_matrices(A_transposed, A)[1]
    columns_A_transposed_b = multiply_matrices(A_transposed, b)[1]

    identity = identity_matrix(columns_A_transposed_A)

    A_inverted = matrix_inverse(A_transposed_A, identity)

    x = multiply_matrices(A_inverted, A_transposed_b)[0]

    return x

def transform_file_to_list(A, b, approximation, rows, columns, df, column_names):
    for outer_index in range(rows):
        list_A = []
        list_b = []
        if df.loc[outer_index, column_names[columns - 1]] != approximation:
            continue
        for inner_index in range(columns - 1):
            list_A.append(df.loc[outer_index, column_names[inner_index]])
        if approximation == 0:
            list_b.append(2)
        else:
            list_b.append(1)

        A.append(list_A)
        b.append(list_b)

    return A, b

def main():
    df = pd.read_excel(dirGr + '/questao_extra.xlsx')

    rows = len(df.index)
    columns = len(df.columns)

    column_names = list(df.columns)

    A_0 = []
    b_0 = []
    A_1 = []
    b_1 = []

    A_0, b_0 = transform_file_to_list(A_0, b_0, 0, rows, columns, df, column_names)
    A_1, b_1 = transform_file_to_list(A_1, b_1, 1, rows, columns, df, column_names)

    coefficients_0 = least_squares(A_0, b_0)
    coefficients_1 = least_squares(A_1, b_1)

    return coefficients_0, coefficients_1

def test():
    coefficients_0, coefficients_1 = main()
    input_list = [None] * 11
    result = 0

    input_list[0] = float(input('Please enter your age: '))
    input_list[1] = float(input('Please enter "0" if you do not have anemia and "1" if you have: '))
    input_list[2] = float(input('Please enter your creatine phosphokinase level: '))
    input_list[3] = float(input('Please enter "0" if you do not have diabetes and "1" if you have: '))
    input_list[4] = float(input('Please enter your blood ejection fraction: '))
    input_list[5] = float(input('Please enter "0" if you do not have high blood pressure and "1" if you have: '))
    input_list[6] = float(input('Please enter your blood platelets: '))
    input_list[7] = float(input('Please enter your creatinine blood level: '))
    input_list[8] = float(input('Please enter your sodium blood level: '))
    input_list[9] = float(input('Please enter "0" if you are biologically female and "1" if you are biologically male: '))
    input_list[10] = float(input('Please enter "0" if you do not smoke and "1" if you smoke: '))

    result_0 = 0
    result_1 = 0
    for i in range(len(coefficients_1)):
        result_0 = result_0 + input_list[i] * coefficients_0[i][0]
        result_1 = result_1 + input_list[i] * coefficients_1[i][0]

    result_0 = (result_0**2)**0.5
    result_1 = (result_1**2)**0.5

    if result_0 > result_1:
        return 'The patient will die'
    else:
        return 'The patient will not die'


print(test())
