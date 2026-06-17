"""  digit_sum is a helper function that perfoms Amstrong Sum .
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number   
"""
def digit_sum (number , total_digit_number ):
    sum_digit = 0
    power = total_digit_number
    while total_digit_number > 0 :
        digit_of_number = number % 10 
        sum_digit += digit_of_number**power 
        number //=10 # new value of the argument number
        total_digit_number -=  1 # Avoid infinity loop
    return sum_digit

def is_armstrong_number(number):
    total_digit_of_number = len(str(number))
    sum_digit = digit_sum(number , total_digit_of_number)
    return sum_digit == number
