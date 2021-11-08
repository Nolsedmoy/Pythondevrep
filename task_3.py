class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        diff = self.parts - other.parts
        if diff >= 0:
            return Cell(diff)
        else:
            print("Ошибка вычитания!")

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, count):
        s = ""
        for i in range(self.parts // count):
            s += '*' * count + '\n'
        s += '*' * (self.parts % count) + '\n'
        return s

    def __str__(self):
        return f'{self.parts}'


cell = Cell(16)
print(cell.make_order(10))
cell_2 = Cell(25)
print(cell_2.make_order(6))

print(cell - cell_2)
print(cell + cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell_2 - cell)
