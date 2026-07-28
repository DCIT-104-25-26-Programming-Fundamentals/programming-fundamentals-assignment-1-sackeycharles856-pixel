def read_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        while True:
            try:
                values = input(f"Enter row {row_index + 1}: ").split()
                if len(values) != columns:
                    print(f"Please enter exactly {columns} numbers.")
                    continue
                matrix.append([int(value) for value in values])
                break
            except ValueError:
                print("Please enter only integers.")
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:>5}" for value in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]


def add_matrices(matrix_a, matrix_b):
    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for column in range(len(matrix_a[0])):
            new_row.append(matrix_a[row][column] + matrix_b[row][column])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])

    result = [[0 for _ in range(columns_b)] for _ in range(rows_a)]

    for row in range(rows_a):
        for col in range(columns_b):
            total = 0
            for inner in range(columns_a):
                total += matrix_a[row][inner] * matrix_b[inner][col]
            result[row][col] = total

    return result


def part_a():
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    matrix = read_matrix(rows, columns)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))


def part_b():
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    print("Enter matrix A:")
    matrix_a = read_matrix(rows, columns)
    print("Enter matrix B:")
    matrix_b = read_matrix(rows, columns)

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nSum:")
    display_matrix(add_matrices(matrix_a, matrix_b))


def part_c():
    try:
        rows_a = int(input("Enter number of rows for matrix A: "))
        columns_a = int(input("Enter number of columns for matrix A: "))
        rows_b = int(input("Enter number of rows for matrix B: "))
        columns_b = int(input("Enter number of columns for matrix B: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    if columns_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    print("Enter matrix A:")
    matrix_a = read_matrix(rows_a, columns_a)
    print("Enter matrix B:")
    matrix_b = read_matrix(rows_b, columns_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nProduct:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))


def main():
    part_a()
    print()
    part_b()
    print()
    part_c()


if __name__ == "__main__":
    main()

