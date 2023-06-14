def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        lists = []
        for num in range(len(col)):
            lists.append(col[num] ** 2)
        new_matrix.append(lists)
    return new_matrix

