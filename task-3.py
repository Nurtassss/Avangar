class Number:
    def __init__(self, number: int):
        self.number = number

    def __add__(self, other):
        self_number = self.number if isinstance(self, Number) else self
       

        return Number(self.number + other.number)

    def __radd__(self, other):
        other_number = other.number if isinstance(other,Number) else other

        return Number(self.number + other_number)

    def __iadd__(self, other):
        other_number = other.number if isinstance(other, Number) else other

        return Number(self.number + other_number)

    def __rsub__(self, other):
        other_number =other.number if isinstance(other, Number)

    def __str__(self):
        return str(self.number)

if __name__ == "__main__":
    num1 = Number(5)
    num2 = Number(6)

    num1 += 10

    print(num1 + num2)
    print(10 + num2)
    print(num1 + 13)
