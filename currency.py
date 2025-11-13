class Currency:
    def __init__(self, amount, unit):
        self.__amount = amount
        self.__unit = unit

    def __eq__(self, other):
        return self.__amount == other.__amount and self.__unit == other.__unit


amount1 = int(input("Enter amount for first currency: "))
unit1 = input("Enter unit for first currency: ")

amount2 = int(input("Enter amount for second currency: "))
unit2 = input("Enter unit for second currency: ")


c1 = Currency(amount1, unit1)
c2 = Currency(amount2, unit2)


if c1 == c2:
    print("Both currencies are equal.")
else:
    print("Currencies are not equal.")
