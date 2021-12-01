a = input("Введите натуральное число: ")
if a.isdigit():
    n = 0
    for i in range(0, (len(a)) - 1):
        if a[i] == a[i + 1]:
            n += 1
    if n == 0:
        print('Нет.')
    else:
        print('Да.')
else:
    print("Это не натуральное число")
