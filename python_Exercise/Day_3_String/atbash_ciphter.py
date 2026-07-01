"""
Create an implementation of the Atbash cipher, an ancient encryption system created     in the Middle East.
"""
import string 

PLAIN = string.ascii_lowercase
CIPHER = list(reversed(string.ascii_lowercase))
LOOK_UP = str.maketrans(dict(zip(PLAIN,CIPHER)))
PUNCTUATION = string.punctuation


def encode(plain_text):
    
    """    
        encode (function) : translate latin word/sentence to cipher word/sentence
          
        - Args :
              - plain_text (str) : latin word
        - Returns:
              - cipher (str) : cipher word of plain_text
    """
    count = 0
    cipher_string = "".join(plain_text.lower().translate(LOOK_UP).split()) # cipher string but with punctuation 
    cipher = ""
      
    for letter in cipher_string :
        if letter.isalnum():
            if count < 5 :
                cipher += letter
                count += 1
            else :
                cipher += " "+letter
                count = 1
                  
    return cipher
      
def decode(ciphered_text):
    """    
        decode (function) : translate cipher word/sentence to latin word/sentence
        - Args :
            - ciphered_text (str) :  ciphered text of a latin text
        - Returns:
            - latin text (str) : latin text that match ciphered text
    """   
    
    return "".join(ciphered_text.translate(LOOK_UP).split())
