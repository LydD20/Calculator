from decimal import Decimal
from calculator import Official_Calculator

class Calculation:
#initialize calculation
    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a=a
        self.b=b
        self.operation=operation

    @staticmethod
    #Creates calculation object
    def create(a: Decimal, b: Decimal, operation):
        return Calculation(a,b, operation)
    
    def perform(self) -> Decimal:
    #performs calculations and returns result
        return self.operation(self.a, self.b)

    def __repr__(self):
    #provides string  representation of calculation
        return f"Calculaion{self.a}, {self.b}, {self.operation.__name__})"
