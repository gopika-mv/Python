class Engine:
    def __init__(self, power):
        self._power = power

class Wheels:
    def __init__(self, size):
        self._size = size

class Car(Engine, Wheels):
    def __init__(self, model, power, size):
        Engine.__init__(self, power)
        Wheels.__init__(self, size)
        self._model = model

    def display(self):
        print(f"Car Model: {self._model}")
        print(f"Power: {self._power} HP")
        print(f"Wheel Size: {self._size} inches")

# Example
c = Car("Tesla Model 3", 400, 18)
c.display()
