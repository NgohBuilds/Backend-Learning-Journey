"""
    Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
    The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet         using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to         modular arithmetic. The letter is shifted for as many values as the value of the key.
"""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def to_cipher (letter , cipher_key):
    """
        to_cipher() transform normal letter to cipher .
    """
    index_of_letter = ALPHABET.find(letter.lower())
    index_of_cipher = (index_of_letter + cipher_key) % len(ALPHABET)
    return ALPHABET[index_of_cipher]
            
def rotate(text, key):
    """
        rotate() transform normal text to cipher text.
    """
    translate_text =""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                translate_text+=to_cipher(letter , key).upper()
            else:
                translate_text+=to_cipher(letter , key)
        else:
            translate_text+=letter
    return translate_text