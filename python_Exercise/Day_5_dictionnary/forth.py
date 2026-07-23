"""Forth Challenge."""
def dup(stack):
    """Duplicate element at the top of stack."""
    
    stack.append(stack[-1])
    return stack
def drop(stack):
    """Pop element at the top of stack."""
    stack.pop()
    return stack
def swap(stack):
    """Given a stack of n elements, swap elements at the position n-1 and n-2."""

    last = len(stack) - 1
    before_last = len(stack) - 2
    tmp = last
    stack[last] = stack[before_last]
    stack[before_last] = stack[tmp]
    
    return stack
def over(stack):
    elt_before_last = stack[-2]
    stack.append(elt_before_last)
    return stack
def is_digit(string):
    try :
        s = int(string)
        return True
    except ValueError:
        return False
def divide (a, b):
    if b == 0:
        raise ZeroDivisionError("divide by zero")
    return a // b
def add(a,b):
    return a + b
def minus(a,b):
    return a - b
def multiply(a,b):
    return a * b
def is_stack_len_right(stack):
    if len(stack) < 2 :
        raise StackUnderflowError("Insufficient number of items in stack")
    return False
    
OP = {
    "+" : add ,
    "-" : minus,
    "*" : multiply,
    "/" : divide
}

class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    """Simulate an evaluator for a very simple subset of Forth."""

    # Cas 1 : On peut effectuer des operations simples
    
    stack = []
    for elt in input_data:
        tokens = elt.split(" ")
        
        for token in tokens:
            if is_digit(token):
                stack.append(int(token))
            else:
                # Gere tous les cas avec les operations
                if not is_stack_len_right(stack):
                    last = stack.pop()
                    before_last = stack.pop()
                    result = OP[token](before_last, last)
                    stack.append(result)
                # Ne reste plus qu'a gerer le cas avec les manip de la stack
                # Ne reste plus qu'a gerer le cas avec les mots definis du user
                    
    return stack
            
                
    
