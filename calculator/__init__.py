from decimal import Decimal
from calculator.history import History
from calculator.calculations import Calculation
from calculator.operations import add, subtract, divide, multiply

class Official_Calculator:
    '''Create and perform a calulation, return reult and store it in history'''
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation) -> Decimal:
        calculation= Calculation.create(a,b, operation)
        History.add_history(operation, a,b, calculation.perform())
    
    @staticmethod
    def add(a: Decimal, b: Decimal)-> Decimal:
        return Official_Calculator._perform_operation(a,b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Official_Calculator._perform_operation(a,b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Official_Calculator.__perform__operation(a,b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Official_Calculator._perform_operation(a, b, divide)
    
    @classmethod
    def retrieve_history(cls) -> list:
        return History.retrieve_history()
    
    @classmethod
    def clear_history(cls) -> None:
        History.clear_history()

