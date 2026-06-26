"""Roman Numeral convertissor exercise from exercism.org"""
ROMAN_TABLE = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def roman(number):
    result = ""

    for value, symbol in ROMAN_TABLE:
        while number >= value:
            result += symbol
            number -= value

    return result

print(roman(3888))