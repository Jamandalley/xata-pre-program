class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        if a == 0:
            return 0
        else:
            return a / b
    
    def square(self, a):
        if a == 0:
            return 0
        else:
            return a ** 2

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        else:
            return a ** 0.5

