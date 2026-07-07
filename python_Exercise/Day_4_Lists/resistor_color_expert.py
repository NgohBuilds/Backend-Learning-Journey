"""resistor_ color_expert.py"""
COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"]
TOLERANCE = {
    "grey" :  "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"}
UNITS = ["ohms",  "kiloohms",  "megaohms", "gigaohms"]

def format_bands(code, color_tolerance, zeros):
    """Format_bands."""
    tolerance = TOLERANCE[color_tolerance]
    code *= 10**zeros
    unit = 0 # x unit (ohms, kiloohms, ...)
    result = code 

    while result >= 1000:
        result /= 1000
        unit += 1
        
    return f"{result:g} {UNITS[unit]} {tolerance}"
    
       
def resistor_label(colors):
    """returns colors label"""
    if len(colors) == 1 :
        return f"{COLORS.index(colors[0])} ohms"
        
    result = 0
    bands = len(colors) - 2   
    
    for unit, color in enumerate(colors[:bands]) :
        result += COLORS.index(color) * 10**(bands - unit - 1)   
        
    multiplier = COLORS.index(colors[bands])
    encoded = format_bands(result, colors[-1], multiplier)

    return encoded