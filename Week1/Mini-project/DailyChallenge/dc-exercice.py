import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area():.2f})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# Tests
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)
c4 = Circle(3)

print(c1)                        # __str__
print(c1.area())                 # area
print(c1 + c2)                   # __add__
print(c1 > c2)                   # __gt__
print(c2 == c4)                  # __eq__

circles = [c3, c1, c4, c2]
print(sorted(circles))          