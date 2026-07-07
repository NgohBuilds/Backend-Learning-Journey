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
TOLERANCE = {"grey" :  "0.05%",
"violet" : "0.1%",
"blue" : "0.25%",
"green" : "0.5%",
"brown" : "1%",
"red" : "2%",
"gold" : "5%",
"silver" : "10%"}
UNITS = ["ohms",  "kiloohms",  "megaohms", "gigaohms"]
def catch_units(input_string):
    zero_catch = (input_string[1:]).count('0')
    first_part = input_string[ : (len(input_string) - zero_catch)] 
    if len(first_part) > 4:
         first_part = first_part[0]+ "." +first_part[1:]
         
    return first_part+ "0"*(zero_catch % 3) + " " + UNITS[zero_catch // 3]+" "
        
    
def resistor_label(colors):
    results = ""
    number_zero = 0
    
    for color in colors[ : (len(colors) - 2)]:
        results += f"{COLORS.index(color)}"
    results+= "0"*COLORS.index(colors[2])
    results = catch_units(results) + f"±{TOLERANCE[colors[-1]]}"
    return results
        
    
