import math

class Calculator:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, other):
        return Calculator(self.angka + other.angka)
    
    def __sub__(self, other):
        return Calculator(self.angka - other.angka)
    
    def __mul__(self, other):
        return Calculator(self.angka * other.angka)
    
    def __truediv__(self, other):
        if other.angka == 0:
            raise ValueError("Division by zero is not allowed")
        return Calculator(self.angka / other.angka)
    
    def __pow__(self, other):
        return Calculator(self.angka ** other.angka)
    
    def log(self, base=math.e):
        if self.angka <= 0:
            raise ValueError("Logarithm is undefined for zero or negative numbers")
        return Calculator(math.log(self.angka, base))
    
    def __repr__(self):
        return f"Calculator({self.angka})"


x = Calculator(10)
y = Calculator(2)

print(x + y)  
print(x - y)  
print(x * y)  
print(x / y) 
print(x ** y)
print(x.log(10))
