def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        lists = []
        for num in range(len(col)):
            lists.append(col[num] ** 2)
        new_matrix.append(lists)
    return new_matrix

def multiply_list_map(my_list=[], number=0):
    lists = my_list.copy()
    new_list[] = lists.map(element => element * number)
    return new_list

def roman_to_int(roman_string):
    numeric, roman_dict = 0, {'I' : 1, 'V' : 5, 'X': 10, 'L' : 50,
              'M' : 1000, 'D' : 500, 'C' : 100, 'IX' : 9}
    size = len(roman_string)
    if size != 0 and roman_string.alpha():
        for r_num in roman_string:
            if r_num.upper() in roman_dict.keys():
                numeric += roman_dict.values()
    return numeric

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
