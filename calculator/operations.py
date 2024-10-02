from decimal import Decimal
'''Code for adding'''
def add (a: Decimal, b: Decimal) -> Decimal:
       return a + b

'''Code for subtracting'''
def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

    '''Code for multiplying'''
def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a*b

'''Code for dividing'''
def divide(a: Decimal, b: Decimal) -> Decimal:
    if b==0:
        raise ValueError ("Sorry, the value of b must be >0 to divide")
    return a/b

