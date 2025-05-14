#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    else:
        result = 0
        compare = 0
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    for i in roman_string:
        if conversion[i] > compare:
            compare = conversion[i] - compare
        else:
            compare = conversion[i]
        result += compare
    return result
