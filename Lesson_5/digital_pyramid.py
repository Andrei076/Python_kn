number = input("Input number from 3 to 9: ")
if number.isdigit() and 2 < int(number) < 10:   # проверка на соответствия натурального числа и диапазона
    for i in range(1, int(number) + 1):
        for j in range(1, i + 1):
            print(j, end="")  # Печатаем по нарастающей
        for j in range(i - 1, 0, -1):
            print(j, end="")  # Печатаем по убывающей
        print()  # создаем переход на следующую строку
else:
    print("Condition not met")
