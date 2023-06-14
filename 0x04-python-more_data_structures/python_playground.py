def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        lists = []
        for num in range(len(col)):
            lists.append(col[num] ** 2)
        new_matrix.append(lists)
    return new_matrix

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary

def multiply_by_2(a_dictionary):
    dict_copy = {}
    for key, value in a_dictionary.items():
        dict_copy[key] = value * 2
    return dict_copy

def best_score(a_dictionary):
    best, key_best = 0, ""
    if len(a_dictionary) == 0:
        return None
    for key, value in a_dictionary.items():
        if value > best:
            best = value
            key_best = key
    return key_best

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
