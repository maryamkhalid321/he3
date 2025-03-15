import math

class Hexagon:
    """Base class for a hexagon"""
    def __init__(self, side):
        self.side = side  # Encapsulation of side length

    def area(self):
        """Calculate the area of a regular hexagon"""
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2

class IrregularHexagon(Hexagon):
    """Derived class for an irregular hexagon"""
    def __init__(self, sides):
        if len(sides) != 6:
            raise ValueError("A hexagon must have exactly 6 sides")
        self.sides = sides  # Encapsulation of different side lengths

    def area(self):
        """Calculate the area using an approximation (divide into 6 triangles)"""
        s = sum(self.sides) / 6  # Approximate side length
        return (3 * math.sqrt(3) * (s ** 2)) / 2  # Approximation formula

# Example usage:
regular_hex = Hexagon(5)  # Regular hexagon with side length 5
print("Regular Hexagon Area:", regular_hex.area())

irregular_hex = IrregularHexagon([4, 5, 4, 5, 4, 5])  # Irregular hexagon
print("Irregular Hexagon Approximate Area:", irregular_hex.area())
