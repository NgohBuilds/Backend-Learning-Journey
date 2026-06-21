BRACKETS = "({[]})"
def is_par_opened (bracket):
    """
        Determine if bracket list start by opened bracket
    """
    return bracket.startswith("[") or bracket.startswith("(") or  bracket.startswith("{")
def store_bracket(string):
    """ Analyse string , collect brackets and return a string with brackets :
        Exemple :    store_bracket ({hello}world([3*5])) => "({}([]))" 
    """
    bracket_stored =""
    for char in string:
        if char in BRACKETS:
            bracket_stored+=char
    return bracket_stored

def alter_ego (bracket):
    if(bracket == "("):
        return ")"
    if(bracket == "["):
        return "]"
    if(bracket == "{"):
        return "}"
    
def is_paired(input_string):
    """ Check if brackets are paired in the right order """
    input_string_bracket = store_bracket(input_string)    # List of bracket in input_string
    if len(input_string_bracket) > 0 and len(input_string_bracket) % 2 == 0 :
        if is_par_opened(input_string_bracket):
            
            """ String start by any bracket ( , { , [ """
            # for index , bracket in enumerate(input_string_bracket) :
                
            #     if bracket == input_string_bracket[]
            
            
        # else:
        #     return False
        # first_list = [0: len(input_string_bracket)/2]
        # second_list = [len(input_string_bracket) / 2 : ]
        # zipped_list_of_brackets = zip(first_list , second_list)
    return False 
        

    
        
    
    
