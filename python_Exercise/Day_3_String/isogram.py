def has_repeated_letter_in_string(string):
    """Check if each letter in string is different """

    new_string = string.lower()
    starting_letter = 0
    while starting_letter < len(new_string) -1 :
        if new_string[starting_letter] in new_string[starting_letter + 1:] :
            return True
        starting_letter+=1
    return False
    
def is_isogram(string):
    """
        EXAMPLE OF ISOGRAMS :
        - lumberjacks : no letter don't repeat l u m b e r j a c k s
        - six-year-old : hyphens are ignored 
        - "" : no letter is isogram

        EXAMPLE OF NOT ISOGRAMS :
        - isograms : letter "s" appear twice 
        - however : letter "e" appear twice 
        - Alpha : a repeat even if "A" and "a" are in different case  
    """
    # Ignore special char :
    new_string= string.replace("-","")
    new_string = new_string.replace(" ","")

    # Check if new_string is empty:
    if not new_string:
        return True
    # result
    return not has_repeated_letter_in_string(new_string)
            
            
            
    

            
            

        
        
    
            
