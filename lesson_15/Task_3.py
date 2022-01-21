class TriangleChecker:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):
        try:
            self.side1 = float(self.side1)
            self.side2 = float(self.side2)
            self.side3 = float(self.side3)
        except Exception:
            return "Нужно вводить только числа!"
        if self.side1 < 0 or self.side2 < 0 or self.side3 < 0:
            return "С отрицательными числами ничего не выйдет!"
        if self.side1 < self.side2 + self.side3 and self.side2 < self.side1 + \
                self.side3 and self.side3 < self.side2 + self.side1:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


my_triangle1 = TriangleChecker(5, 6, "ff")
print(my_triangle1.is_triangle())
my_triangle2 = TriangleChecker(5, 6, 8)
print(my_triangle2.is_triangle())
my_triangle3 = TriangleChecker(5, 6, -2)
print(my_triangle3.is_triangle())
my_triangle4 = TriangleChecker(5, 6, 20)
print(my_triangle4.is_triangle())
