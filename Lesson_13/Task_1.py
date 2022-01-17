def my_concatenation():
    number_1 = input("Введите первое значение: ")
    number_2 = input("Введите второе значение: ")
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        number_1 = str(number_1)
        number_2 = str(number_2)
        summa_str = number_1 + number_2
        print(f"Конкатенация:  {summa_str}")
    else:
        summa_int = number_1 + number_2
        print(f"Сумма чисел = {summa_int}")


my_concatenation()
