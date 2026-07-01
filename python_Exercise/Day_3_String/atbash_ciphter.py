"""
Create an implementation of the Atbash cipher, an ancient encryption system created     in the Middle East.
"""
import string 

PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]
LOOK_UP = str.maketrans(dict(zip(PLAIN,CIPHER)))


def encode(plain_text):
    
    """    
        encode (function) : translate latin word/sentence to cipher word/sentence
          
        - Args :
              - plain_text (str) : latin word
        - Returns:
              - cipher (str) : cipher word of plain_text
    """
    count = 0
    encoded = "".join(plain_text.lower().translate(LOOK_UP).split())  
    cipher = ""
      
    for letter in encoded :
        if letter.isalnum():
            if count == 5 :
                cipher += " "
                count = 0
           
            cipher += letter
            count += 1
                  
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
