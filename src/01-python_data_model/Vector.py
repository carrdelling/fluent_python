from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        _x = self.x + other.x
        _y = self.y + other.y

        return Vector(_x, _y)

    def __mul__(self, scalar):
        _x = self.x * scalar
        _y = self.y * scalar

        return Vector(_x, _y)

    def __repr__(self):
        return 'Vector({!r},{!r})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)


short = Vector(1, 2)
long = Vector(5, 7)
longer = short + long

print(longer)
longer += short
modulo = abs(longer)
print('This is even longer:')
print(longer)
print(modulo)

three_times = short * 3
print(three_times)

zero = Vector()

if not zero:
    print('This is a zeroed vector')
