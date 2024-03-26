#!/usr/bin/python3
def max_integer(my_list=[]):
    """my_list.sort()
    return my_list[len(my_list) - 1]
    """
    max_value = my_list[0]
    for i in range(0, len(my_list)):
        if max_value < my_list[i]:
            max_value = my_list[i]
    return max_value
