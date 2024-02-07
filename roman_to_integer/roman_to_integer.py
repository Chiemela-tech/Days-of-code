# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

#The first solution
def romanToInt(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for symbol in s:
        print(f"Examining letter: {symbol}")
        value = roman_values[symbol]
        print(f"Current Value: {value}")
        if value > prev_value:
            print(f"Previous Value: {prev_value}")
            result += value - 2 * prev_value
            print(f"result from if statement: {result}")
        else:
            result += value #result = result + value
            print(f"result when if statement didn't run: {result} {value}")
        prev_value = value
        print(f"previous value after if else: {prev_value}")

    return result



# The second solution
def romansToInt(s: str) -> int:
        romans_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for character in s:
            number += romans_values[character]
        return number

print(romansToInt("MMMCMXCIX")) 