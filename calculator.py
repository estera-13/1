class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        return self.op1 + self.op2

    def subtract(self):
        return self.op1 - self.op2

    def multiply(self):
        return self.op1 * self.op2

    def divide(self):
        if self.op2 == 0:
            print('Nie można dzielić przez 0!')
            return None
        return self.op1 / self.op2



# Przykład 1
if __name__ == '__main__':
    wynik1 = Calculator(10, 5)
    print(wynik1.sum())
    print(wynik1.subtract())
    print(wynik1.multiply())
    print(wynik1.divide())

# Przykład 2
    wynik2 = Calculator(13, 0)
    print(wynik2.divide())
class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        return self.op1 + self.op2

    def subtract(self):
        return self.op1 - self.op2

    def multiply(self):
        return self.op1 * self.op2

    def divide(self):
        if self.op2 == 0:
            print('Nie można dzielić przez 0!')
            return None
        return self.op1 / self.op2



# Przykład 1
if __name__ == '__main__':
    wynik1 = Calculator(10, 5)
    print(wynik1.sum())
    print(wynik1.subtract())
    print(wynik1.multiply())
    print(wynik1.divide())

# Przykład 2
    wynik2 = Calculator(13, 0)
    print(wynik2.divide())
