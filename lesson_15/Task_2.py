class Group:
    def __init__(self):
        self.students = []

    def from_student(self, name, age, grades):
        self.students.append(Student(name, age, grades))

    def show_group(self):
        for i in self.students:
            i.show_student()


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    # Функция выводит только имена и оценки студентов
    def show_student(self):
        print(f"Имя: {self.name}\t Оценки: {self.grades}")


my_group = Group()
my_group.from_student("Daniel", 20, [5, 5, 5, 4])
my_group.from_student("Inga", 25, [5, 2, 3])
my_group.from_student("Peter", 23, [4, 3, 2])
my_group.from_student("Oleg", 30, [2, 5, 5])
my_group.show_group()
