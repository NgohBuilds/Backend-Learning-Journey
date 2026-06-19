"""Pangram"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(sentence):
    """
    Check if a sentence is pangram . 
         ===================================================================
    Note : A pangram is a sentence using every letter of the alphabet at least once.
    It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
    """

    if not sentence:
        return False
        
    count = 0
    new_sentence = sentence.lower()
    for letter in ALPHABET:
        if letter in new_sentence:
            count += 1
            
    return count == len(ALPHABET)
    
