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
    str_format_code = str(code)
    tolerance = TOLERANCE[color_tolerance] 
    code *= 10**(zeros % 3)
    zeros -= zeros % 3
    unit = zeros // 3 # x unit (ohms, kiloohms, ...)
    result = code * 10**zeros
    if len(str(result)) >= 4:
        result = result * 10**-3
        unit += 1
    return f"{result:g} {UNITS[unit]} {tolerance}"
    
    
    
def resistor_label(colors):
    """Blable."""
    result = 0
    bands = (len(colors) // 2) + (len(colors) % 2)
    
    for unit, color in enumerate(colors[:bands]) :
        result += COLORS.index(color) * 10**(bands - unit - 1)
     
    multiplier = COLORS.index(colors[bands]) # Color at 3rd or 4th position
    # result *= 10 ** multiplier
    encoded = format_bands(result, colors[bands + 1], multiplier)
    return encoded