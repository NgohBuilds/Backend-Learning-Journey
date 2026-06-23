""" Some text """
COLORS = {"black": 0,"brown": 1,"red":2,"orange": 3,"yellow": 4,"green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9}
EQUIVALENT = {"0":" ohms","3":" kiloohms", "6":" megaohms","9":" gigaohms"}

def label(colors):
    """label function : translating the colors into a label"""
    two_first_digit = COLORS[colors[0]]*10 + COLORS[colors[1]]
    number_of_zero = COLORS [colors[2]]
    if COLORS[colors[1]] == 0:
        number_of_zero = COLORS [colors[2]] + 1 
        two_first_digit = COLORS[colors[0]]
        if COLORS[colors[0]]==0:
            two_first_digit=""
    return str(two_first_digit)+ "0"*(number_of_zero % 3)+EQUIVALENT[str(number_of_zero - number_of_zero % 3)]