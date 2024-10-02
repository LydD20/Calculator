#I'm still trying to understand how history actually works.
#This is my current code but I plan to go back and work on it a bit.
#This is the best success I've had with my code.
from decimal import Decimal
'''Keeps history of calculations'''
class History:
    history=[] #store in a list

'''Adds to history list'''
@classmethod
def add_history(cls, calculation: str, a: Decimal, b: Decimal, result: Decimal):
    cls.history.append({
        'operation': object,
        'oper1' : a,
        'oper2' : b,
        'result': result
    })

'''Retrieves history'''
@classmethod
def retrieve_history(cls) -> list:
    return cls.history

'''Clears History'''
@classmethod
def clear_histoty(cls) -> None:
    cls.history.clear()