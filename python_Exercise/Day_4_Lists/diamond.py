""" Some text """
ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
def make_diamond (letter , space_around_letter):
    """
        Draw diamond specified in instruction
    """
    upper_triangle = []
    for index_ltr , ltr in enumerate(ALPHABET [0 : ALPHABET.index(letter.upper()) + 1]):
        lines_char = ""
        if index_ltr == 0 :
            lines_char =  " "*space_around_letter+ltr+ " "*space_around_letter
        else:
            space_side_letter = space_around_letter - index_ltr
            space_between_pair_letter = 2*(index_ltr  -1) + 1
            lines_char = " "*(space_side_letter)+ ltr + " "*( space_between_pair_letter ) + ltr + " "*(space_side_letter) # diamond rows (correct rows)
        upper_triangle.append(lines_char)
    lower_triangle = upper_triangle[0:]
    lower_triangle.pop()
    lower_triangle.reverse() 
    upper_triangle.extend(lower_triangle)
    return upper_triangle
        
def rows(letter):
    """
        Code test => (> | <)    
    """
    rows_number = 2 * ALPHABET.index(letter.upper()) + 1
    space_around_letter = (rows_number - 1) // 2
    if rows_number == 1:
        return [letter]
    return make_diamond(letter , space_around_letter)

print(rows("c"))
"""
    def rows(letter: str) -> List[str]:
    letters = [chr(k) for k in range(ord('A'), ord(letter) + 1)]
    alphabet = letters[:-1] + letters[::-1]
    diamond_line = letters[::-1] + letters[1:]
    return [''.join(x if x == y else ' ' for y in diamond_line) for x in alphabet]
"""