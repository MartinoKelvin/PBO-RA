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
            raise ValueError("tidak boleh dibagi 0")
        return Calculator(self.angka / other.angka)
    
    def __pow__(self, other):
        return Calculator(self.angka ** other.angka)
    
    def log(self, base=math.e):
        if self.angka <= 0:
            raise ValueError("log tidak bisa dengan 0 atau bilangan negatif")
        return Calculator(math.log(self.angka, base))
    
    def __repr__(self):
        return str(self.angka) 

x = Calculator(10)
y = Calculator(2)

print(x + y)  
print(x - y)  
print(x * y)  
print(x / y)  
print(x ** y) 
print(x.log(10))
