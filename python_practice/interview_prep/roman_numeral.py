roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
numeral_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def int_to_roman(num):
    if num > 3999 or num < 1:
        return "Invalid argument"
    string_builder = ''
    i = 0
    while num > 0:
        if num - numeral_val[i] >= 0:
            string_builder = string_builder + (roman_numerals[i])
            num -= numeral_val[i]
        else:
            i += 1
    return string_builder

print (int_to_roman(55))