#!/usr/bin/python3
for digit1 in range(9):
    for digit2 in range(10):
        if (digit1 == 8) and (digit2 == 9):
            print("{}{}".format(digit1, digit2))
        elif (digit2 > digit1):
            print(digit1, end="")
            print(digit2, end=", ")
