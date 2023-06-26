#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
            continue
        except (ValueError, TypeError):
            ans = 0
            print("wrong type")
            continue
        except IndexError:
            ans = 0
            print("out of range")
            continue
        finally:
            new_list.append(ans)
    return new_list
