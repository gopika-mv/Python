class Rectangle:
    def __init__(self, l=1, b=1):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __gt__(self, other):
        return self.area() > other.area()

    def __str__(self):
        return f"Length = {self.length}, Breadth = {self.breadth}, Area = {self.area()}, Perimeter = {self.perimeter()}"


try:
    print("Enter details for Rectangle 1:")
    l1 = int(input("Enter length: "))
    b1 = int(input("Enter breadth: "))
    r1 = Rectangle(l1, b1)

    print("\nEnter details for Rectangle 2:")
    l2 = int(input("Enter length: "))
    b2 = int(input("Enter breadth: "))
    r2 = Rectangle(l2, b2)

    print("\n Rectangle 1 \n", r1)
    print("\n Rectangle 2 \n",r2)

    if r1 > r2:
        print("\nRectangle 1 has a larger area.")
    elif r2 > r1:
        print("\nRectangle 2 has a larger area.")
    else:
        print("\nBoth rectangles have equal area.")

except Exception as e:
    print("Error:", e)
