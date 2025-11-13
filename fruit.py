class FruitBasket:
    def __init__(self, fruit_name, price_per_kg):
        self.fruit_name = fruit_name
        self.price_per_kg = price_per_kg

    def __add__(self, other):
        unique_fruits = {}
        for f, p in {**self.fruit_name, **other.fruit_name}.items():
            if f in self.fruit_name and f in other.fruit_name:
                unique_fruits[f] = min(self.fruit_name[f], other.fruit_name[f])
            else:
                unique_fruits[f] = p
        return FruitBasket(unique_fruits, None)

    def display(self):
        for fruit, price in self.fruit_name.items():
            print(f"{fruit}: ₹{price}")


b1 = FruitBasket({'apple': 120, 'banana': 40}, None)
b2 = FruitBasket({'apple': 100, 'orange': 80}, None)
b3 = b1 + b2
b3.display()
