""" Some text """

COLOR_VALUES = {"black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,"green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,
}
EQUIVALENT = {0:" ohms",3:" kiloohms", 6:" megaohms",9:" gigaohms"}


def label(colors):
    """label function : translate the colors in arguement into a label."""
    
    first_digit_value , second_digit_value ,number_of_zero  = [COLOR_VALUES[color] for color in colors[:3]]
    two_first_digit = first_digit_value * 10 + second_digit_value
    
    if two_first_digit == 0 : 
        return "0 ohms"
        
    if two_first_digit  % 10 == 0:  # two_first = 10
        number_of_zero += 1
        two_first_digit = first_digit_value
        
    remaining_zero = number_of_zero % 3
    zero_suit = '0'*(remaining_zero)

    return f"{two_first_digit}{zero_suit}{EQUIVALENT[number_of_zero - remaining_zero]}"

