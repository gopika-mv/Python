class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __gt__(self, other):
        return self.__age > other.__age


p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

if p1 > p2:
    print("Alice is older")
else:
    print("Bob is older")
