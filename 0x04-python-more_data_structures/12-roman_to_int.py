#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str:
        result = 0
        numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
                   'V': 5, 'I': 1}
        charnum = 0
        while (charnum < len(roman_string)):
            char = roman_string[charnum]
            if char in numbers:
                next_value = 0
                if (charnum + 1) < len(roman_string):
                    next_value = numbers[roman_string[charnum + 1]]
                if numbers[char] < next_value:
                    result += next_value - numbers[char]
                    charnum += 1
                else:
                    result += numbers[char]
            else:
                break
            charnum += 1
        return result
    else:
        return 0
