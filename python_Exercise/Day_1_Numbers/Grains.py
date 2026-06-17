"""Some text"""
def square(number):
    """A function that returns the number of grain in given square number(arguement) 
    
    Number of grains for each square : 
        square 1 -> 1 ->2^0
        square 2 -> 1*2 -> 2^1
        square 3 -> 1*2*2 -> 2^2
        square 4 -> 1*2*2*2 -> 2^3
        ...
        square n -> 1*2*...*2 -> 2^(n - 1)
    """
    if(number<=0 or number >64):
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)

def total():
    my_sum = 0
    for number in range(1,65):
        my_sum = my_sum + square(number)
    return my_sum