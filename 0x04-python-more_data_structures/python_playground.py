def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        lists = []
        for num in range(len(col)):
            lists.append(col[num] ** 2)
        new_matrix.append(lists)
    return new_matrix

def weight_average(my_list=[]):
    avg, div = 0, 0
    if len(my_list) != 0:
        for tuples in my_list:
            if len(tuples) < 2:
                tuples += (0, 0)
            avg = tuples[0] * tuples[1]
            div += tuples[1]
        avg /= div
    return avg
