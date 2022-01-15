"""Модуль в котором находятся три функции: pair_finding, prime_generator, solve
"""


def pair_finding(x, y):
    """Функция которая принимает на вход параметры : список чисел любой
   длины и число . Функция должна проверить есть ли в списке 2 числа сумма
   которых еквивалентна числу переданому 2м параметром."""
    g = 0
    for a in x:
        g += 1
        for b in x[g::]:
            if (a + b) == y:
                return print('Есть пара для сумы')
    else:
        return print("Комбинаций не выявлено")


def prime_generator(x, y):
    """Функция генератор простых чисел в дипазоне заданых 2мя аргументами чисел.
    """
    for num in range(x + 1, y):
        count = 0
        d = 2
        while d < num:
            if num % d == 0:
                count += 1
            d += 1
        if count == 0:
            yield num


def solve(s):
    """Функция принимает список,создает пустой список, находит элементы с
    четным индексом (включая 0) и заносит их в созданный список и возвращает его
    """
    c = []
    for i in range(len(s)-1):
        if i == 0 or i % 2 == 0:
            c.append(s[i])
    return c
