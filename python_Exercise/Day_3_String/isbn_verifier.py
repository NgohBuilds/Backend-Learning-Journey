"""isbn_verifier"""
DIGIT_MULTIPLIER_RATE = 10
def calculate_isbn_validity (isbn):
    """
     Calculate validity isbn with this formula
        (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1)
    """
    result = 0
    for index , digit in enumerate(isbn[:-1]):
        result += int(digit) * (DIGIT_MULTIPLIER_RATE - index)
    if isbn[-1].isdigit():
        return result + int(isbn[-1])
    return result
    
    
        
def is_valid(isbn):
    """
        Given an ISBN code , function must determine if it's valid :
        PROCESS :

        1. Create a function that use isbn formula check validity
        2. Verify the length of isbn without hyphens (len(isbn)==10)
        3. Verify if each character in isbn are digits 
          -> Yes : call function for check validity (step 1)
          -> No : go to next step
        4. Verify if each char in   the first digits subsequence (9) are digits 
          -> Yes : Check last char type (if yes => result of validity test || if no => return False)
          -> No : return False 
    """
    isbn_with_out_hyphens= isbn.replace("-","")
    if len(isbn_with_out_hyphens) == 10: 
        if isbn_with_out_hyphens.isdigit():
            return calculate_isbn_validity(isbn_with_out_hyphens) % 11 == 0
        if(isbn_with_out_hyphens[:-1]).isdigit():
            if isbn_with_out_hyphens.endswith("X"):
                return (calculate_isbn_validity(isbn_with_out_hyphens) + DIGIT_MULTIPLIER_RATE) % 11 == 0
    return False
    

        
