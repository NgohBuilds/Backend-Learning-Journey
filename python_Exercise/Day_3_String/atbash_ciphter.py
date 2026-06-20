PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER ="zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    cipher_text = ""
    max_letter = 5
    for letter in plain_text.lower():
        if letter.isalpha():
            if len(cipher_text) < max_letter :
                cipher_text+=CIPHER[PLAIN.find(letter)]
            else:
                if letter.isalpha():
                    cipher_text+=" "+CIPHER[PLAIN.find(letter)]
                else:
                    cipher_text+=" "+letter
                max_letter = len(cipher_text) + 4
        else:
                if letter.isalpha():
                    cipher_text+=" "+CIPHER[PLAIN.find(letter)]
                else:
                    cipher_text+=" "+letter
                max_letter = len(cipher_text) + 4
    return cipher_text

def decode(ciphered_text):
    pass
