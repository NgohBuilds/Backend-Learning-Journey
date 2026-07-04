"""ETL challenge"""
def transform(legacy_data):
    """Transform a legacy score dictionary into the new format.

        Arg :
            legacy_data (dict)
            
        returns :
            comprehension dictionary (dict)    
    """
    return {letter.lower() : point  
            for point, letters in legacy_data.items() 
            for letter in letters
            } 