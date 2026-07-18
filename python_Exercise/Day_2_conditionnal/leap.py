"""leap challenge 
    @uthor : gabrielngoh
    Date : 18/07/2026
"""
def leap_year(year):
    """determine if given year is a leap year """
    return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)