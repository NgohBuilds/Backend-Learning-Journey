"""
    isempty () : check if a string is empty 
    delete_lines () : return a string without lines (\n , \t , ...)
"""
def isempty(text):
    return text.strip() ==""
def delete_lines(text):
    return " ".join(text.splitlines())

def response(hey_bob):
    """
        Give Bob's answers
   """

    if isempty(hey_bob):
        return "Fine. Be that way!"

    text = delete_lines(hey_bob.strip())

    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if text.isupper():
        return "Whoa, chill out!"

    if text.endswith("?"):
        return "Sure."

    return "Whatever."