""" Word_count challenge from exercism """
import re

def count_words(sentence):
    """
    Count_words takes sentence as 1 argument and return a dictionnary where keys are word of     the sentence and values are the occurence of the key in the sentence
    """
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence.lower())

    result = {}
    
    for word in words:
        result[word] = result.get(word, 0) + 1

    return result