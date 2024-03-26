#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checklist = []
    for i in range(len(my_list)):
        if (my_list[i] % 2):
            checklist += [False]
        else:
            checklist += [True]
    return checklist
