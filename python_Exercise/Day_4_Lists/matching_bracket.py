"""Matching_brackets challenge."""
BRACKETS = {"[" : "]", "(" : ")", "{" : "}"}
    
def is_paired(input_string):
    """ Check if brackets are paired in the right order """
    stack = []
    
    for bracket in input_string:
        
        if bracket in BRACKETS:
            stack.append(bracket)
        elif bracket in BRACKETS.values():
            
            if not stack  or bracket != BRACKETS[stack.pop()]:
                return False
       
    return not stack

print(is_paired("{[)][]}"))     # result : False
print(is_paired("(((185 + 223.85) * 15) - 543)/2"))  # result : True
print(is_paired("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{x} &... x^2 \\end{array}\\right)")) # result : True