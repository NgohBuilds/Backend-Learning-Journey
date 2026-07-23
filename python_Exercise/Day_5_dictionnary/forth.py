"""Forth Challenge."""

def is_operation (op):
    if op not in OP:
        raise ValueError("undefined operation")
    return op

def dup(stack):
    """Duplicate element at the top of stack."""
    if not stack:
        raise StackUnderflowError("Insufficient number of items in stack")
        
    stack.append(stack[-1])
    return stack  

def drop(stack):
    """Pop element at the top of stack."""
    if not stack:
        raise StackUnderflowError("Insufficient number of items in stack")
        
    stack.pop()
    return stack

def swap(stack):
    """Given a stack of n elements, swap elements at the position n-1 and n-2."""
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    stack[-1], stack[-2] = stack[-2], stack[-1]
    return stack

def over(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
   
    elt_before_last = stack[-2]
    stack.append(elt_before_last)
    return stack

def is_digit(string):
    try :
        s = int(string)
        return True
    except ValueError:
        return False

def divide (stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
        
    last, before_last = stack.pop(), stack.pop()
    if last == 0:
        raise ZeroDivisionError("divide by zero")
    stack.append(before_last // last)
    return stack   

def add(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    last, before_last = stack.pop(), stack.pop()
    stack.append(last + before_last)
    return stack

def minus(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    last, before_last = stack.pop(), stack.pop()
    stack.append(before_last - last)
    return stack

def multiply(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    last, before_last = stack.pop(), stack.pop()
    stack.append(last * before_last)
    return stack

OP = {
    "+" : add ,
    "-" : minus,
    "*" : multiply,
    "/" : divide,
    "dup" : dup,
    "drop" : drop,
    "swap" : swap,
    "over" : over   
}


class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    """Simulate an evaluator for a very simple subset of Forth."""
    stack = []
    for elt in input_data:
        # Definir la nature de elt :
        #  Si Mot personnalisé > [ :<name> (built-in op | number| customised_name)]
        
        #  Si Mot non personnalisé
        tokens = elt.split(" ")
        for token in tokens:
            if is_digit(token):
                stack.append(int(token))
            else:
                uniformised_token = is_operation(token.lower())
                stack = OP[uniformised_token](stack) 
                    
    return stack