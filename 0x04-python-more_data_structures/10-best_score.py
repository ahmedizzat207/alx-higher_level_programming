#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        check = 0
        for key in list(a_dictionary):
            if check == 0:
                best_key = key
                check = 1
            if a_dictionary[key] > a_dictionary[best_key]:
                best_key = key
        return best_key
    else:
        return None
