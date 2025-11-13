import math

class Complex:
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag

    def magnitude(self):
        return math.sqrt(self.__real ** 2 + self.__imag ** 2)

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def display(self):
        print("Complex Number:", self.__real, "+", self.__imag, "i")

# Input from user
r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part of first complex number: "))
r2 = int(input("Enter real part of second complex number: "))
i2 = int(input("Enter imaginary part of second complex number: "))


c1 = Complex(r1, i1)
c2 = Complex(r2, i2)


c1.display()
c2.display()


if c1 >= c2:
    print("First complex number is greater or equal.")
else:
    print("Second complex number is greater.")
