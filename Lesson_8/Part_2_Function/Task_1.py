# Вариант №1
def func3(x, y):
    g = 0
    for a in x:
        g += 1
        for b in x[g::]:
            if (a + b) == y:
                return print('Есть пара для сумы')
    else:
        return print("Комбинаций не выявлено")


func3([1, 2.5, 3, 4, 10, 3.5, 4], 7)

func3([1, 2, 3, 4, 5, 6], 100)

# Вариант №2
# def fun_po(a_list, p):
#     t = 0
#     t1 = 0
#     for i in a_list:
#         t += 1
#         for j in a_list[t::]:
#             if int(i) + int(j) == p:
#                 t1 += 1
#
#     if t1 > 0:
#         s = bool(True)
#     else:
#         s = bool(False)
#     return s
#
#
# a = 0
# b = 1
# c_list = []
# print('введите список состоящий из чисел, для завершения введите любую букву')
# while a == 0:
#     k = input(f' введите {b}-ое число списка ')
#     if str(k).isdigit():
#         c_list.append(k)
#         b += 1
#     elif str(k).isalpha() and b < 3:
#         print('Вы ввели не правильно. Повторите.')
#     else:
#         a += 1
#
# m = int(input('введите число k: '))
# if fun_po(c_list, m):
#     print('Есть пара для суммы')
# else:
#     print('Комбинаций не выявлено')
