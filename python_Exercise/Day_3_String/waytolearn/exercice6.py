"""Exercice from waytolearn"""
def delete_char (index, string):
    """delete n-th char of a string"""

    return  string[:index] + string[index + 1 :] 



print(delete_char(10, 'hello'))