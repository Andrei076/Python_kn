class NumericCounter:
    counter = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = start

    def increase(self):
        if self.counter < self.end:
            self.counter += 1
            return f"Счетчик увеличился на единицу: {self.counter}"
        else:
            return 'Достигнут максимум'

    def show(self):
        return f"Значение счетчика: {self.counter}"

    def reset(self):
        self.counter = self.start
        return "Счетчик сброшен в начальное значение"


my_counter = NumericCounter(4, 6)
print(my_counter.increase())
print(my_counter.increase())
print(my_counter.increase())
print(my_counter.show())
print(my_counter.reset())
print(my_counter.show())
