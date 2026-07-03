"""Secret_handshake challenge """

COMMANDS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    """commands : function that returns a list of command according to arg value """
    handshake = [
        COMMANDS[bit_index]
        for bit_index in range(len(COMMANDS)) 
        if binary_str[-1 - bit_index] == "1"]
    
    return handshake[::-1] if binary_str[0] == "1" else handshake 
